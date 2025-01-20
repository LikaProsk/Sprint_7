import json

import allure
import requests
from requests import Response

from config import base_url
from logic.base_class_logic import BaseClassLogic


class CourierLoginLogic(BaseClassLogic):

    @allure.step('Авторизация курьера')
    def courier_authorization(self, login: str, password: str):
        payload = {
            "login": login,
            "password": password
        }

        response = requests.post(f'{base_url}/api/v1/courier/login', data=payload)

        return response

    @allure.step('Проверка успешной авторизации курьера')
    def check_courier_authorization(self, response: Response):
        self.check_response_status_code(response, 200)

        result = json.loads(response.text)
        assert 'id' in result and result.get('id') is not None and isinstance(result.get('id'), int), \
            'Не удалось авторизоваться'

    @allure.step('Получение id курьера')
    def get_courier_id(self, response: Response):
        result = json.loads(response.text)
        return result.get('id')
