import requests
from .. import Client


class SevUser:
    def __init__(self, user) -> None:
        self._user = user

    @property
    def id(self):
        return self._user["id"]


class SevDesk:
    @staticmethod
    def user(client: Client):
        url = f"{client.base_url}/SevUser"

        request = requests.get(url=url, headers=client.get_headers())
        request.raise_for_status()

        user = request.json()["objects"]
        return SevUser(user[0])

    @staticmethod
    def raise_for_status(response, operation: str):
        if not response.status_code == 200 and not response.status_code == 201:
            raise IOError(
                f"Operation {operation} failed with status code: {response.status_code}."
            )
