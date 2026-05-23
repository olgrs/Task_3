import allure
from pages.base_page import BasePage
from locators.feed_page_locators import *


class FeedPage(BasePage):

    @allure.step("Клик по первому заказу в ленте")
    def click_first_order(self):
        self.click_to_element(("xpath", ORDER_IN_FEED))

    def wait_for_first_order(self, timeout=15):
        self.wait_for_element_present(("xpath", ORDER_IN_FEED), timeout)

    def wait_for_order_number(self, order_number, timeout=25):
        self.wait_for_element_present(("xpath", f"//p[contains(text(), '{order_number}')]"), timeout)

    def wait_for_counters(self, timeout=10):
        self.wait_for_element_present(("xpath", COUNTER_ALL_TIME), timeout)

    def wait_for_order_in_work(self, order_number, timeout=20):
        self.wait_for_text_in_element(("xpath", ORDER_IN_WORK), order_number, timeout)

    @allure.step("Получить ID заказа из модального окна")
    def get_order_id_from_modal(self):
        return self.get_text_from_element(("xpath", TEXT_ORDER_ID))

    @allure.step("Получить счетчик 'Выполнено за всё время'")
    def get_counter_all_time(self):
        return self.get_text_from_element(("xpath", COUNTER_ALL_TIME))

    @allure.step("Получить счетчик 'Выполнено за сегодня'")
    def get_counter_today(self):
        return self.get_text_from_element(("xpath", COUNTER_TODAY))

    @allure.step("Получить номер заказа в разделе 'В работе'")
    def get_order_in_work(self):
        return self.get_text_from_element(("xpath", ORDER_IN_WORK))