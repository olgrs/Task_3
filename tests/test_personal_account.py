import allure


class TestPersonalAccount:

    @allure.title("Переход по клику на «Личный кабинет»")
    def test_navigate_to_personal_account(self, main_page, login_page, profile_page, test_user):
        email, password, token = test_user
        main_page.click_login_button()
        login_page.login(email, password)
        main_page.click_personal_account()
        assert profile_page.is_element_displayed(
            ("xpath", "//p[text()='В этом разделе вы можете изменить свои персональные данные']")
        ), "Не удалось перейти в личный кабинет"

    @allure.title("Переход в раздел «История заказов»")
    def test_navigate_to_order_history(self, main_page, login_page, profile_page, test_user):
        email, password, token = test_user
        main_page.click_login_button()
        login_page.login(email, password)
        main_page.click_personal_account()
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
        assert login_page.is_element_displayed(("xpath", "//button[text()='Войти']")), (
            "Не удалось выйти из аккаунта"
        )
