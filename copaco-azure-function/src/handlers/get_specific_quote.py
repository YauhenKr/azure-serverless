import logging

import azure.functions as func

from src.exceptions.exceptions import handle_exceptions
from src.services.service import QuoteDataService


@handle_exceptions
def specific_quote(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Function get_specific_quote is processing...')

    quote_service = QuoteDataService()
    filtered_quotes = quote_service.get_specific_quote('les')

    if not filtered_quotes:
        return func.HttpResponse(
            body="There are no one quotes with 'les' in the author",
            status_code=404
        )
    return func.HttpResponse(
        body=f"These are all the quotes with 'les' in the author: {filtered_quotes}",
        status_code=200
    )
