import allure
import pytest

from locators.feed_page_locators import COUNTER_MAP


class TestOrderFeed:

    @allure.title("Открытие всплывающего окна с деталями заказа при клике на заказ в ленте")
    def test_open_order_modal(self, main_page, feed_page):
        main_page.click_order_feed()
        feed_page.open_first_order()
        assert feed_page.is_order_modal_open(), (
            "Не открылось всплывающее окно с деталями заказа"
        )

    @allure.title("Заказы пользователя из 'Истории заказов' отображаются на странице 'Лента заказов'")
    def test_order_in_feed(self, main_page, feed_page, profile_page, logged_in_user):
        main_page.create_order()
        main_page.close_order_modal()
        main_page.open_profile()
        profile_page.open_order_history()
        order_number = profile_page.get_last_order_number()
        main_page.click_order_feed()
        feed_page.wait_order_in_feed(order_number)
        assert feed_page.is_order_in_feed(order_number), (
            f"Заказ с номером {order_number} не найден в ленте заказов"
        )

    @allure.title("После оформления заказа его номер появляется в разделе В работе")
    def test_order_in_work(self, main_page, feed_page, logged_in_user):
        order_number = main_page.create_order().strip()
        main_page.close_order_modal()
        main_page.click_order_feed()
        feed_page.wait_order_in_work(order_number)
        assert feed_page.is_order_in_work(order_number), (
            f"Заказ с номером {order_number} не найден в разделе В работе"
        )

    @allure.title("При создании нового заказа увеличиваются счетчики")
    @pytest.mark.parametrize('locator_name', [
        'COUNTER_ALL_TIME',
        'COUNTER_TODAY'
    ])
    def test_counter_increase(self, main_page, feed_page, locator_name, logged_in_user):
        locator = COUNTER_MAP[locator_name]

        main_page.click_order_feed()
        old_count = feed_page.get_all_time_counter(locator)

        feed_page.open_constructor()
        main_page.create_order()
        main_page.close_order_modal()

        main_page.click_order_feed()
        feed_page.wait_counter_increases(locator, old_count)
        new_count = feed_page.get_all_time_counter(locator)

        assert new_count > old_count, (
            f"Счётчик {locator_name} не увеличился: было {old_count}, стало {new_count}"
        )
