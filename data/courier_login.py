from logic.create_courier_logic import CreateCourierLogic


def get_negative_case():
    courier_logic = CreateCourierLogic()
    courier = courier_logic.register_new_courier_and_return_login_password()

    login = courier.get('login')
    password = courier.get('password')

    test_case = {
        'incorrect_login': {
            'login': 'kmnijnij',
            'password': password,
            'status_code': 404,
            'error_message': "Учетная запись не найдена"
        },
        'incorrect_password': {
            'login': login,
            'password': 'фовчлфоывфоыыфвы',
            'status_code': 404,
            'error_message': "Учетная запись не найдена"
        },
        'empty_login': {
            'login': '',
            'password': password,
            'status_code': 400,
            'error_message': "Недостаточно данных для входа"
        },
        'empty_password': {
            'login': login,
            'password': '',
            'status_code': 400,
            'error_message': "Недостаточно данных для входа"
        }
    }

    return test_case
