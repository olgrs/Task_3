import allure

from locators.profile_page_locators import *
from pages.base_page import BasePage


class ProfilePage(BasePage):

    @allure.step("Клик по кнопке 'История заказов'")
    def open_order_history(self):
        self.click_to_element(BUTTON_ORDER_HISTORY)

    @allure.step("Клик по кнопке 'Выход'")
    def logout(self):
        self.click_to_element(BUTTON_LOGOUT)

    @allure.step("Получение номера последнего заказа")
    def get_last_order_number(self):
        return self.get_text_from_element(ORDER_HISTORY_LAST_NUMBER)
    
    @allure.step("Проверка отображения истории заказов")
    def is_history_opened(self):
        return self.is_element_displayed(ORDER_HISTORY_LIST)
    
    @allure.step("Проверка открытия личного кабинета")
    def is_account_opened(self):
        return self.is_element_displayed(BUTTON_LOGOUT)
