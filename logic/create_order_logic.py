import json

import allure
import requests
from requests import Response

from config import base_url
from logic.base_class_logic import BaseClassLogic


@allure.step('Создание нового заказа')
class CreateOrderLogic(BaseClassLogic):

    def create_order(self,
                     first_name: str,
                     last_name: str,
                     address: str,
                     metro_station: str,
                     phone: str,
                     rent_time: int,
                     delivery_date: str,
                     comment: str,
                     color: list = None):
        payload = {
            "firstName": first_name,
            "lastName": last_name,
            "address": address,
            "metroStation": metro_station,
            "phone": phone,
            "rentTime": rent_time,
            "deliveryDate": delivery_date,
            "comment": comment,
            "color": color if color is not None else []
        }

        response = requests.post(f'{base_url}api/v1/orders', json=payload)

        return response

    @allure.step('Проверка успешного создания нового заказа')
    def check_create_order(self, response: Response):
        self.check_response_status_code(response, 201)

        result = json.loads(response.text)
        assert 'track' in result and result.get('track') is not None and isinstance(result.get('track'),
                                                                                    int), 'Не удалось создать заказ'
