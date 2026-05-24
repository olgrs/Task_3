import allure

from locators.forgot_password_locators import *
from pages.base_page import BasePage


class ForgotPasswordPage(BasePage):

    @allure.step("Ввести email для восстановления")
    def recover(self, email):
        self.add_text_to_element(EMAIL_INPUT, email)
        self.click_to_element(BUTTON_RECOVER)

    @allure.step("Клик по кнопке показать/скрыть пароль")
    def click_show_password(self):
        self.click_to_element(BUTTON_SHOW_PASSWORD)

    @allure.step("Проверить, что отображается страница восстановления пароля")
    def is_password_recovery_page_displayed(self):
        return self.is_element_displayed(PAGE_TITLE)

    @allure.step("Дождаться появления поля для нового пароля")
    def wait_for_new_password_input(self):
        return self.is_element_displayed(PASSWORD_INPUT)

    @allure.step("Проверить, что поле ввода нового пароля отображается")
    def is_new_password_input_displayed(self):
        return self.is_element_displayed(PASSWORD_FIELD_ACTIVE)
