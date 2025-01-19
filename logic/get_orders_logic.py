import json

import allure
import requests
from requests import Response

from config import base_url
from logic.base_class_logic import BaseClassLogic


class GetOrdersLogic(BaseClassLogic):

    @allure.step('Получение списка заказов')
    def get_orders(self,
                   courier_id: int = None,
                   nearest_station: str = None,
                   limit: int = None,
                   page: int = None):

        url = f'{base_url}api/v1/orders'

        params = {}

        if courier_id is not None:
            params.update({"courierId": courier_id})

        if nearest_station is not None:
            params.update({"nearestStation": nearest_station})

        if limit is not None:
            params.update({"limit": limit})

        if page is not None:
            params.update({"page": page})

        response = requests.get(url, params=params)

        return response

    @allure.step('Проверка наличия списка заказов в ответе метода')
    def check_list_of_orders(self, response: Response):
        self.check_response_status_code(response, 200)

        result = json.loads(response.text)
        assert 'orders' in result and len(result.get('orders')) > 0, 'Не удалось получить список заказов'
