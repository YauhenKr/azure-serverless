import httpx
import logging
import random

from typing import List, Optional

from src.schemas.schema import Quote


class QuoteDataService:
    _API_URL = "https://api.quotable.io"
    _page_numbers = None

    @classmethod
    def get_random_quote(cls) -> Quote:
        """
        This method aims to retrieve random quote from the API
        :return: it returns random quote
        """
        logging.info('Trying to retrieve random quote...')
        url = f"{cls._API_URL}/quotes/random"
        data = cls._make_request(url)
        return Quote(
            id=data[0]["_id"], content=data[0]["content"], author=data[0]["author"]
        )

    @classmethod
    def get_all_quotes(cls) -> Optional[List[Quote]]:
        """
        This method aims to retrieve list of quotes from the API
        :return: list of quotes from the API
        """
        logging.info('Trying to retrieve array of quotes...')

        common_url = f"{cls._API_URL}/quotes"
        data = cls._make_request(common_url)
        total_amount_of_pages = data.get('totalPages')

        logging.info(f'Total amount of pages is {total_amount_of_pages}')

        if total_amount_of_pages >= 10:
            cls._page_numbers = random.sample(range(1, total_amount_of_pages + 1), 10)
        else:
            cls._page_numbers = random.sample(range(1, total_amount_of_pages + 1), total_amount_of_pages)

        quotes = cls.retrieve_over_pages()
        return quotes

    @classmethod
    def retrieve_over_pages(cls) -> list:
        """
        Method to get over all random pages
        :return: list of Quote
        """
        quotes = []
        for page in cls._page_numbers:
            logging.info(f'Processing page one by one...{page} from {cls._page_numbers}')
            try:
                url = f"{cls._API_URL}/quotes?page={page}"
                data = cls._make_request(url)
                quotes_per_page = [
                    Quote(
                        id=quote_data["_id"],
                        content=quote_data["content"],
                        author=quote_data["author"]) for quote_data in data["results"]
                ]
                quotes.extend(quotes_per_page)
            except KeyError as error:
                raise {f"During processing the {error} was occurred"}

        return quotes

    @classmethod
    def get_specific_quote(cls, parameter: str) -> [List, None]:
        """
        This method aims to process array of unfiltered quotes by specified parameter
        :param parameter: to search by it
        :return: list of filtered quotes
        """
        quotes = cls.get_all_quotes()
        filtered_quotes = [
            quote.dict() for quote in quotes if parameter in quote.dict().get("author").lower()
        ]

        if not filtered_quotes:
            return None
        return filtered_quotes

    @staticmethod
    def _make_request(url: str) -> [dict, str]:
        """
        Method makes a request to url and return the response with data
        :param url: takes the API's url
        :return: array of data from the particular API
        """
        logging.info('Trying to connect to API...')

        with httpx.Client() as client:
            logging.info('Client is connected...')

            response = client.get(url)
            if response.status_code != 200:
                return f"Response text during the connection: {response.text}"

            data = response.json()
            logging.info(f'Returning the data: {data}')

            return data
