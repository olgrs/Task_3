import allure
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from locators.feed_page_locators import *


class FeedPage(BasePage):

    @allure.step("Клик по первому заказу в ленте")
    def click_first_order(self):
        self.click_to_element(("xpath", ORDER_IN_FEED))

    def wait_for_first_order(self, timeout=15):
        self.wait_for_element_present(("xpath", ORDER_IN_FEED), timeout)

    def wait_for_order_number(self, order_number, timeout=60):
        locator = ("xpath", f"//*[contains(text(), '{order_number}')]")
        self.wait_for_element_visible(locator, timeout)

    def wait_for_counters(self, timeout=10):
        self.wait.until(EC.presence_of_all_elements_located(("xpath", ORDER_FEED_NUMBER)))
        elements = self.find_elements(("xpath", ORDER_FEED_NUMBER))
        if len(elements) < 2:
            raise TimeoutException("Счётчики не найдены")

    def get_counter_all_time(self):
        return self.find_elements(("xpath", ORDER_FEED_NUMBER))[0].text

    def get_counter_today(self):
        return self.find_elements(("xpath", ORDER_FEED_NUMBER))[1].text

    @allure.step("Получить ID заказа из модального окна")
    def get_order_id_from_modal(self):
        return self.get_text_from_element(("xpath", TEXT_ORDER_ID))

    @allure.step("Получить номер заказа в разделе 'В работе'")
    def get_order_in_work(self):
        return self.get_text_from_element(("xpath", ORDER_IN_WORK))

    def is_order_displayed(self, order_number):
        return self.is_element_displayed(("xpath", ORDER_NUMBER.format(order_number)))
