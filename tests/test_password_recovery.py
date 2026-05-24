import allure


class TestPasswordRecovery:

    @allure.title("Переход на страницу восстановления пароля по кнопке «Восстановить пароль»")
    def test_open_recovery(self, main_page, login_page, forgot_password_page):
        main_page.click_login_button()
        login_page.click_forgot_password()
        assert forgot_password_page.is_password_recovery_page_displayed(), (
            "Не удалось перейти на страницу восстановления пароля"
        )

    @allure.title("Ввод почты и клик по кнопке «Восстановить»")
    def test_recover_password(self, main_page, login_page, forgot_password_page):
        main_page.click_login_button()
        login_page.click_forgot_password()
        forgot_password_page.recover("test@example.com")
        assert forgot_password_page.wait_for_new_password_input(), (
            "Не удалось перейти на страницу сброса пароля"
        )

    @allure.title("Клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его")
    def test_toggle_password(self, main_page, login_page, forgot_password_page):
        main_page.click_login_button()
        login_page.click_forgot_password()
        forgot_password_page.recover("test@example.com")
        forgot_password_page.click_show_password()
        assert forgot_password_page.is_new_password_input_displayed(), (
            "Поле пароля не подсвечено после клика по кнопке показать/скрыть пароль"
        )
