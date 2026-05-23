import allure
from data import BASE_URL
from pages.base_page import BasePage
from locators.login_page_locators import *


class LoginPage(BasePage):

    @allure.step("Ввести email")
    def enter_email(self, email):
        self.add_text_to_element(("xpath", EMAIL_INPUT), email)

    @allure.step("Ввести пароль")
    def enter_password(self, password):
        self.add_text_to_element(("xpath", PASSWORD_INPUT), password)

    @allure.step("Клик по кнопке 'Войти'")
    def click_login(self):
        self.click_to_element(("xpath", BUTTON_LOGIN))

    @allure.step("Клик по кнопке 'Зарегистрироваться'")
    def click_register(self):
        self.click_to_element(("xpath", BUTTON_REGISTER))

    @allure.step("Клик по кнопке 'Восстановить пароль'")
    def click_forgot_password(self):
        self.click_to_element(("xpath", BUTTON_FORGOT_PASSWORD))

    @allure.step("Залогиниться: email и пароль")
    def login(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_login()
        self.wait_for_url_to_be(BASE_URL)
