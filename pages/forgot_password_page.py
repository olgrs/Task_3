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
        return self.find_element_with_wait(("xpath", PASSWORD_FIELD_ACTIVE)).is_displayed()
