import functools
import requests

from azure.functions import HttpRequest, HttpResponse
from typing import Callable


def handle_exceptions(func: Callable[..., HttpResponse]) -> Callable[..., HttpResponse]:
    @functools.wraps(func)
    def wrapper(*args: HttpRequest, **kwargs: HttpRequest) -> HttpResponse:
        try:
            return func(*args, **kwargs)
        except requests.RequestException as e:
            error_message = f"Error occurred while retrieving the quotes: {str(e)}"
            return HttpResponse(body=error_message, status_code=400)
    return wrapper
