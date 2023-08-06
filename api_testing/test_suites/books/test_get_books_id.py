

from http import HTTPStatus
from api_testing.business.books.api.books_api import BooksAPI
import pytest
import allure

class TestCase:

    booksAPI = BooksAPI()

    @allure.title("[P0][Negative] Invalid id")
    def test_get_books_validId_p0(self):
        Id = 5
        Title = "Book 5"
        Description = "Lorem lorem lorem. Lorem lorem lorem. Lorem lorem lorem.\n"
        PageCount = 500

        res = self.booksAPI.books_id(
            id=Id,
        )

        assert res.status_code == HTTPStatus.OK

        resp = res.json()
        assert resp["id"] == Id
        assert resp["title"] == Title
        assert resp["description"] == Description
        assert resp["pageCount"] == PageCount

    @allure.title("[P3][Negative] Without symbol hash ")
    def test_get_books_url_withHash_p3(self):
        Id = "#"
        Id0 = 1
        Title0 = "Book 1"

        res = self.booksAPI.books_id(
            id=Id,
        )

        assert res.status_code == HTTPStatus.OK

        resp = res.json()
        assert resp["id"][0] == Id0
        assert resp["title"][0] == Title0
