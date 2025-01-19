import allure
import pytest

from data.courier_login import get_negative_case
from logic.courier_login_logic import CourierLoginLogic
from logic.create_courier_logic import CreateCourierLogic


class TestCourierLogin:

    @allure.title('Проверка успешной авторизации курьера')
    @allure.description('Для успешной авторизации курьера передаем уникальные логин и пароль')
    def test_courier_successful_authorization_positive(self):
        courier_logic = CreateCourierLogic()
        login_and_password = courier_logic.register_new_courier_and_return_login_password()
        courier_login = CourierLoginLogic()
        response = courier_login.courier_authorization(login_and_password.get('login'),
                                                       login_and_password.get('password'))
        courier_login.check_courier_authorization(response)

    @allure.title('Проверка ошибки при некорректных, нeсуществующих данных или их отсутствии')
    @allure.description(
        'Для получения ошибки передаем некорректные, несуществующие логин и пароль, либо вообще их не передаем')
    @pytest.mark.parametrize('case', get_negative_case().values(), ids=get_negative_case().keys())
    def test_authorization_with_incorrect_values_negative(self, case: dict):
        courier_login = CourierLoginLogic()
        response = courier_login.courier_authorization(case.get('login'), case.get('password'))
        courier_login.check_response_status_code(response, case.get('status_code'))
        courier_login.check_error_message(response, case.get('error_message'))
