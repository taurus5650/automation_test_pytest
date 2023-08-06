from ...api_request import APIRequest
from api_testing.configurations.domain import FakeRestAPIConfig
from urllib.parse import urljoin


class BooksAPI (APIRequest):
    BASE_URL = FakeRestAPIConfig.URL

    BOOKS = "/api/v1/Books"

    def __init__(self, waitingTime=5):
        super().__init__(waitingTime=waitingTime)

    def books_id(self, id):
        headers = {
            "accept": "*/*",
            "Content-Type": "application/json; v=1.0"
        }

        return self._sendRequest(
            method="GET",
            url=urljoin(self.BASE_URL, self.BOOKS + f"/{id}"),
            headers=headers,
        )
