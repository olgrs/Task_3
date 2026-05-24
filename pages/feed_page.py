import allure

from data import FEED_URL
from locators.feed_page_locators import *
from pages.base_page import BasePage


class FeedPage(BasePage):
    @allure.step("Открыть страницу списка заказов")
    def open(self):
        self.go_to_url(FEED_URL)

    @allure.step("Клик по первому заказу в ленте")
    def open_first_order(self):
        self.click_to_element(ORDER_IN_FEED_LAST)

    @allure.step("Отобажение модального окна заказа")
    def is_order_modal_open(self):
        return self.is_element_displayed(MODAL_ORDER_DETAILS)

    @allure.step("Получение счетчика заказов")
    def get_all_time_counter(self, locator):
        self.wait_for_element_to_be_visible(locator)
        return int(self.get_text_from_element(locator))

    @allure.step("Получение локатора заказа")
    def get_order_locator(self, locator_template, order_number):
        locator = (
            locator_template[0],
            locator_template[1].format(order_number)
        )
        return locator

    @allure.step("Ожидание появления заказа")
    def wait_order(self, locator_template, order_number, timeout=30):

        self.wait_for_element_to_be_visible(
            self.get_order_locator(locator_template, order_number),
            timeout
        )

    @allure.step("Ожидание заказа в ленте")
    def wait_order_in_feed(self, order_number, timeout=30):
        self.wait_order(ORDER_IN_FEED, order_number, timeout)

    @allure.step("Ожидание заказа в работе")
    def wait_order_in_work(self, order_number, timeout=60):
        expected = f"0{order_number}"
        self.wait_order(ORDER_IN_WORK, expected, timeout)

    @allure.step("Проверка заказа в ленте")
    def is_order_in_feed(self, order_number):
        return self.is_order_displayed(ORDER_IN_FEED, order_number)

    @allure.step("Проверка заказа в работе")
    def is_order_in_work(self, order_number):
        expected = f"0{order_number}"
        return self.is_order_displayed(ORDER_IN_WORK, expected)

    @allure.step("Проверка отображения заказа")
    def is_order_displayed(self, locator_template, order_number):
        result = self.is_element_displayed(
            self.get_order_locator(locator_template, order_number)
        )
        return result

    @allure.step("Проверка отображения ленты заказов")
    def is_feed_displayed(self):
        return self.is_element_displayed(ORDER_FEED_HEADING)
