import json

import allure


class BaseClassLogic:

    @allure.step('Проверка статус кода ответа')
    def check_response_status_code(self, response, status_code: int):
        assert response.status_code == status_code, "Статус кода ответа не соответствует ожидаемому"

    @allure.step('Проверка сообщения об ошибке в ответе')
    def check_error_message(self, response, error_message):
        response = json.loads(response.text)
        assert response.get('message') == error_message, ('Сообщение об ошибке не соответствует ожидаемому\n'
                                                          f'Ожидаемый результат: {error_message}\n'
                                                          f'Фактический результат: {response.get("message")}')
