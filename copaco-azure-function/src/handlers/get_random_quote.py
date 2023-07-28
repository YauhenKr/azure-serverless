import json
import logging

import azure.functions as func

from src.exceptions.exceptions import handle_exceptions
from src.services.service import QuoteDataService


@handle_exceptions
def random_quote(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Function get_random_quote is processing...')

    quote_service = QuoteDataService()
    one_random_quote = quote_service.get_random_quote()

    if not one_random_quote:
        return func.HttpResponse(
            body="There is no one quote",
            status_code=404
        )
    return func.HttpResponse(
        body=json.dumps(one_random_quote.dict()),
        status_code=200
    )
