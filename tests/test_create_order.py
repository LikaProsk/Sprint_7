import allure
import pytest

import data.create_order as create_order_data
from logic.create_order_logic import CreateOrderLogic


class TestCreateOrder:

    @allure.title('Проверка успешного сценария создания заказа с разными цветами самоката')
    @allure.description('Для успешного создания заказа заполняем все поля и выбираем разные цвета самоката')
    @pytest.mark.parametrize('color', [['BLACK'], ['GREY', 'BLACK'], []])
    def test_create_order_successfully_positive(self, color):
        create_order = CreateOrderLogic()
        response = create_order.create_order(create_order_data.first_name,
                                             create_order_data.last_name,
                                             create_order_data.address,
                                             create_order_data.metro_station,
                                             create_order_data.phone,
                                             create_order_data.rent_time,
                                             create_order_data.delivery_date,
                                             create_order_data.comment,
                                             color
                                             )
        create_order.check_create_order(response)
