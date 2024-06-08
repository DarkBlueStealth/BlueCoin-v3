from .exceptions import BlueCoinException

def handle_response(response):
    if response.status_code == 200:
        return response.json()
    else:
        try:
            error_message = response.json().get('message', 'An unknown error occurred.')
        except ValueError:
            error_message = 'An unknown error occurred.'
        raise BlueCoinException(error_message)

def handle_response_no_error(response):
    return response.json()