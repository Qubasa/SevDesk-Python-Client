from __future__ import annotations

import requests
import attrs
import cattrs

from .. import Client


@attrs.define()
class SevUser:
    id: str

    @staticmethod
    def from_json(data) -> SevUser:
        return cattrs.structure(data, SevUser)


class SevDesk:
    @staticmethod
    def user(client: Client) -> SevUser:
        """
        Get the current SevUser for the given Token
        """
        url = f"{client.base_url}/SevUser"

        request = requests.get(url=url, headers=client.get_headers())
        request.raise_for_status()

        objects = request.json()["objects"][0]
        return SevUser.from_json(objects)

    @staticmethod
    def raise_for_status(response, operation: str):
        if not response.status_code == 200 and not response.status_code == 201:
            raise IOError(
                f"Operation {operation} failed with status code: {response.status_code}."
            )
