import allure
from pages.base_page import BasePage
from locators.profile_page_locators import *
from locators.feed_page_locators import ORDER_LAST_NUMBER


class ProfilePage(BasePage):

    @allure.step("Клик по кнопке 'Профиль'")
    def click_profile(self):
        self.click_to_element(("xpath", BUTTON_PROFILE))

    @allure.step("Клик по кнопке 'История заказов'")
    def click_order_history(self):
        self.click_to_element(("xpath", BUTTON_ORDER_HISTORY))

    @allure.step("Клик по кнопке 'Выход'")
    def click_logout(self):
        self.click_to_element(("xpath", BUTTON_LOGOUT))

    @allure.step("Получить текст профиля")
    def get_profile_text(self):
        return self.get_text_from_element(("xpath", TEXT_PROFILE))

    @allure.step("Получить номер последнего заказа из истории")
    def get_last_order_number(self):
        order_element = self.find_element_with_wait(("xpath", ORDER_LAST_NUMBER))
        return order_element.text

    @allure.step("Дождаться загрузки страницы профиля")
    def wait_for_profile_page(self):
        self.wait_for_url_contains("/account")
