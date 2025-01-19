import allure

from logic.get_orders_logic import GetOrdersLogic


class TestGetOrders:

    @allure.title('Проверка успешного получения списка заказов')
    @allure.description('Для успешного получения списка заказов передаем в URL необходимые параметры')
    def test_get_orders_successfully_positive(self):
        get_orders = GetOrdersLogic()
        response = get_orders.get_orders(nearest_station='["1", "2"]', limit=2, page=0)
        get_orders.check_list_of_orders(response)
