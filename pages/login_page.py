import allure

from locators.login_page_locators import *
from pages.base_page import BasePage


class LoginPage(BasePage):

    @allure.step("Залогиниться по email и паролю")
    def login(self, email, password):
        self.add_text_to_element(EMAIL_INPUT, email)
        self.add_text_to_element(PASSWORD_INPUT, password)
        self.click_to_element(BUTTON_LOGIN)

    @allure.step("Клик по кнопке 'Восстановить пароль'")
    def click_forgot_password(self):
        self.click_to_element(BUTTON_FORGOT_PASSWORD)

    @allure.step("Проверка выхода из аккаунта")
    def is_logged_out(self):
        return self.is_element_displayed(BUTTON_LOGIN)
