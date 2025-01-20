import allure
import requests

from config import base_url
from logic.base_class_logic import BaseClassLogic


class DeleteCourierLogic(BaseClassLogic):

    @allure.step('Удаление курьера')
    def delete_courier(self, id: str):
        url = f'{base_url}/api/v1/courier/:id'

        payload = {"id": id}

        response = requests.delete(url, data=payload)

        return response
