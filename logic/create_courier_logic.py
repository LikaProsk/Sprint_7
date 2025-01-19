import json

import allure
import requests
from requests import Response

from config import base_url
from data.create_courier import generate_random_string
from logic.base_class_logic import BaseClassLogic


class CreateCourierLogic(BaseClassLogic):

    @allure.step('Создание нового курьера')
    def create_courier(self, login: str, password: str, first_name: str):
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        response = requests.post(f'{base_url}api/v1/courier', data=payload)

        return response

    @allure.step('Проверка успешного создания нового курьера')
    def check_success_create_courier(self, response: Response):
        self.check_response_status_code(response, 201)

        response = json.loads(response.text)
        assert response.get('ok'),'Не удалось создать курьера'

    @allure.step('Регистрация нового курьера и получение его логина и пароля')
    def register_new_courier_and_return_login_password(self):

        login = generate_random_string(10)
        password = generate_random_string(10)
        first_name = generate_random_string(10)

        response = self.create_courier(login, password, first_name)

        result = {}

        if response.status_code == 201:
            result = {
                "login": login,
                "password": password,
                "firstName": first_name
            }

        return result