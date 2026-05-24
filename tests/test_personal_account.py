import allure


class TestPersonalAccount:

    @allure.title("Переход по клику на «Личный кабинет»")
    def test_open_account(self, profile_page, logged_in_user):
        profile_page.open_profile()
        assert profile_page.is_account_opened(), (
            "Не удалось перейти в личный кабинет"
        )

    @allure.title("Переход в раздел «История заказов»")
    def test_order_history(self, profile_page, logged_in_user):
        profile_page.open_profile()
        profile_page.open_order_history()
        assert profile_page.is_history_opened(), (
            f"Не удалось перейти в раздел «История заказов», текущий URL: {profile_page.get_current_url()}"
        )

    @allure.title("Выход из аккаунта")
    def test_logout(self, profile_page, login_page, logged_in_user):
        profile_page.open_profile() 
        profile_page.logout()
        assert login_page.is_logged_out(), (
            "Не удалось выйти из аккаунта"
        )
