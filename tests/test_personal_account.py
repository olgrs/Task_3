import allure

from data import LOGIN_URL
from locators.login_page_locators import BUTTON_LOGIN


class TestPersonalAccount:

    @allure.title("Переход по клику на «Личный кабинет»")
    def test_navigate_to_personal_account(self, main_page, login_page, profile_page, test_user):
        email, password, _ = test_user
        main_page.click_login_button()
        login_page.login(email, password)
        main_page.click_personal_account()
        profile_page.wait_for_profile_page()
        assert "/account" in main_page.get_current_url(), "Не удалось перейти в личный кабинет"

    @allure.title("Переход в раздел «История заказов»")
    def test_navigate_to_order_history(self, main_page, login_page, profile_page, test_user):
        email, password, token = test_user
        main_page.click_login_button()
        login_page.login(email, password)
        main_page.click_personal_account()
        profile_page.wait_for_profile_page()
        profile_page.click_order_history()
        assert "/account/order-history" in main_page.get_current_url(), (
            f"Не удалось перейти в раздел «История заказов», текущий URL: {main_page.get_current_url()}"
        )

    @allure.title("Выход из аккаунта")
    def test_logout(self, main_page, login_page, profile_page, test_user):
        email, password, token = test_user
        main_page.click_login_button()
        login_page.login(email, password)
        main_page.click_personal_account()
        profile_page.click_logout()
        main_page.wait_for_url_to_be(LOGIN_URL)
        assert login_page.is_element_displayed(("xpath", BUTTON_LOGIN)), (
            "Не удалось выйти из аккаунта"
        )
