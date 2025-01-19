import allure

from data.create_courier import generate_random_string
from logic.create_courier_logic import CreateCourierLogic


class TestCreateCourier:

    @allure.title('Проверка успешного сценария создания нового курьера')
    @allure.description('Для успешного создания нового курьера при каждом обращении передаем уникальные данные')
    def test_create_new_courier_successfully_positive(self, new_courier_login_password):
        courier_logic = CreateCourierLogic()
        login = new_courier_login_password.get('login')
        password = new_courier_login_password.get('password')
        first_name = new_courier_login_password.get('first_name')

        response = courier_logic.create_courier(login, password, first_name)
        courier_logic.check_success_create_courier(response)

    @allure.title('Проверка ошибки при создании одного и того же курьера')
    @allure.description(
        'Для получения ошибки передаем одинаковые данные для повторного создания одного и того же курьера')
    def test_check_same_courier_twice_negative(self, new_courier_login_password):
        courier_logic = CreateCourierLogic()
        login = new_courier_login_password.get('login')
        password = new_courier_login_password.get('password')
        first_name = new_courier_login_password.get('first_name')

        response = courier_logic.create_courier(login, password, first_name)
        courier_logic.check_success_create_courier(response)

        response = courier_logic.create_courier(login, password, first_name)
        courier_logic.check_response_status_code(response, 409)
        courier_logic.check_error_message(response, 'Этот логин уже используется. Попробуйте другой.')

    @allure.title('Проверка ошибки при создании курьера без заполнения обязательного поля')
    @allure.description('Для получения ошибки  не передаем логин курьера')
    def test_check_courier_creation_without_login_negative(self, new_courier_login_password):
        courier_logic = CreateCourierLogic()
        login = ''
        password = new_courier_login_password.get('password')
        first_name = new_courier_login_password.get('first_name')

        response = courier_logic.create_courier(login, password, first_name)
        courier_logic.check_response_status_code(response, 400)
        courier_logic.check_error_message(response, 'Недостаточно данных для создания учетной записи')

    @allure.title('Проверка ошибки при повторном использовании логина для создания курьера')
    @allure.description('Для получения ошибки  пароль и имя передаем уникальные, а логин повторный')
    def test_check_courier_creation_without_login_negative(self):
        courier_logic = CreateCourierLogic()
        login = generate_random_string(10)

        response = courier_logic.create_courier(login, generate_random_string(10), generate_random_string(10))
        courier_logic.check_success_create_courier(response)

        response = courier_logic.create_courier(login, generate_random_string(10), generate_random_string(10))
        courier_logic.check_response_status_code(response, 409)
        courier_logic.check_error_message(response, 'Этот логин уже используется. Попробуйте другой.')












