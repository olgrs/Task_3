import allure
from pages.base_page import BasePage
from locators.forgot_password_locators import *


class ForgotPasswordPage(BasePage):

    @allure.step("Ввести email для восстановления")
    def enter_email(self, email):
        self.add_text_to_element(("xpath", EMAIL_INPUT), email)

    @allure.step("Клик по кнопке 'Восстановить'")
    def click_recover(self):
        self.click_to_element(("xpath", BUTTON_RECOVER))

    @allure.step("Клик по кнопке показать/скрыть пароль")
    def click_show_password(self):
        self.click_to_element(("xpath", BUTTON_SHOW_PASSWORD))

    @allure.step("Проверить, что поле пароля активно")
    def is_password_field_active(self):
        return self.is_element_displayed(("xpath", PASSWORD_FIELD_ACTIVE))

    @allure.step("Проверить, что отображается страница восстановления пароля")
    def is_password_recovery_page_displayed(self):
        return self.is_element_displayed(("xpath", PAGE_TITLE))

    @allure.step("Дождаться появления поля для нового пароля")
    def wait_for_new_password_input(self):
        self.find_element_with_wait(("xpath", PASSWORD_INPUT))

    @allure.step("Проверить, что поле ввода нового пароля отображается")
    def is_new_password_input_displayed(self):
        return self.is_element_displayed(("xpath", PASSWORD_INPUT))
