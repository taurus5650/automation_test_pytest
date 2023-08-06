

from http import HTTPStatus
from api_testing.business.users.api.users_api import UsersAPI
import random
import pytest
import allure


class TestCase:

    usersAPI = UsersAPI()

    @allure.title("[P0][Negative] Invalid id")
    def test_post_users_validId_p0(self):
        Id = 5
        UserName = "UserTest"
        Password = "PasswordTest"

        res = self.usersAPI.postUsers(
            id=Id,
            userName=UserName,
            password=Password
        )

        assert res.status_code == HTTPStatus.OK

        resp = res.json()
        assert resp["id"] == Id
        assert resp["userName"] == UserName
        assert resp["password"] == Password

    @pytest.mark.skip(reason="Since haven't release.")
    @allure.title("[P2][Positive] userName null")
    def test_post_users_userNameNullalble_p2(self):
        randomNum = random.randint(1, 200)

        Id = randomNum
        UserName = None
        Password = "PasswordTest"

        res = self.usersAPI.postUsers(
            id=Id,
            userName=UserName,
            password=Password
        )

        assert res.status_code == HTTPStatus.OK

        resp = res.json()
        assert resp["id"] == Id
        assert resp["userName"] == UserName
        assert resp["password"] == Password

    @allure.title("[P0][Negative] userName as int")
    def test_post_users_userNameNullalble_p2(self):
        randomNum = random.randint(1, 200)

        Id = randomNum
        UserName = 123
        Password = "PasswordTest"

        res = self.usersAPI.postUsers(
            id=Id,
            userName=UserName,
            password=Password
        )

        assert res.status_code != HTTPStatus.OK
