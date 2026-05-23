import allure
from pages.base_page import BasePage
from locators.profile_page_locators import *


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