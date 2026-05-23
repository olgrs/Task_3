import allure


class TestPasswordRecovery:

    @allure.title("Переход на страницу восстановления пароля по кнопке «Восстановить пароль»")
    def test_navigate_to_forgot_password(self, main_page, login_page, forgot_password_page):
        main_page.click_login_button()
        login_page.click_forgot_password()
        assert forgot_password_page.is_password_recovery_page_displayed(), (
            "Не удалось перейти на страницу восстановления пароля"
        )

    @allure.title("Ввод почты и клик по кнопке «Восстановить»")
    def test_recover_password(self, main_page, login_page, forgot_password_page):
        main_page.click_login_button()
        login_page.click_forgot_password()
        forgot_password_page.enter_email("test@example.com")
        forgot_password_page.click_recover()
        forgot_password_page.wait_for_new_password_input()
        assert forgot_password_page.is_new_password_input_displayed(), (
            "Не удалось перейти на страницу сброса пароля"
        )

    @allure.title("Клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его")
    def test_show_password_highlights_field(self, main_page, login_page, forgot_password_page):
        main_page.click_login_button()
        login_page.click_forgot_password()
        forgot_password_page.enter_email("test@example.com")
        forgot_password_page.click_recover()
        forgot_password_page.click_show_password()
        assert forgot_password_page.is_password_field_active(), (
            "Поле пароля не подсвечено после клика по кнопке показать/скрыть пароль"
        )
