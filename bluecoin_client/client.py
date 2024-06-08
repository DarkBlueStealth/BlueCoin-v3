import requests
from .exceptions import BlueCoinException
from .utils import handle_response, handle_response_no_error

class BlueCoinClient:
    def __init__(self, base_url, no_error_mode=False):
        self.base_url = base_url
        self.no_error_mode = no_error_mode

    def change_password(self, username, current_password, new_password):
        url = f"{self.base_url}/v1/change_password"
        data = {
            "username": username,
            "password": current_password,
            "new_password": new_password
        }
        response = requests.post(url, json=data)
        return self._handle_response(response)

    def create_user(self, username, password):
        url = f"{self.base_url}/v1/create_user"
        data = {
            "username": username,
            "password": password
        }
        response = requests.post(url, json=data)
        return self._handle_response(response)

    def delete_user(self, username, password):
        url = f"{self.base_url}/v1/delete_user"
        data = {
            "username": username,
            "password": password
        }
        response = requests.post(url, json=data)
        return self._handle_response(response)

    def get_balance(self, username):
        url = f"{self.base_url}/v1/get_balance"
        data = {
            "username": username
        }
        response = requests.post(url, json=data)
        return self._handle_response(response)

    def get_transactions(self, username, offset=0):
        url = f"{self.base_url}/v1/get_transactions"
        params = {
            "username": username,
            "offset": offset
        }
        response = requests.get(url, params=params)
        return self._handle_response(response)

    def get_users(self, offset=0):
        url = f"{self.base_url}/v1/get_users"
        params = {
            "offset": offset
        }
        response = requests.get(url, params=params)
        return self._handle_response(response)

    def pow_give(self):
        url = f"{self.base_url}/v1/powgive"
        response = requests.post(url)
        return self._handle_response(response)

    def pow_check(self, username, nonce):
        url = f"{self.base_url}/v1/powcheck"
        data = {
            "username": username,
            "nonce": nonce
        }
        response = requests.post(url, json=data)
        return self._handle_response(response)

    def get_last_mined(self):
        url = f"{self.base_url}/last_mined"
        response = requests.get(url)
        return self._handle_response(response)

    def take_transaction(self, username, password, morsels, recipient, note):
        url = f"{self.base_url}/v1/transaction"
        data = {
            "username": username,
            "password": password,
            "morsels": morsels,
            "recipient": recipient,
            "note": note
        }
        response = requests.post(url, json=data)
        return self._handle_response(response)

    def _handle_response(self, response):
        if self.no_error_mode:
            return response.json()
        else:
            return handle_response(response)