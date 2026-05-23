import allure
from locators.main_page_locators import *


class TestMainFunctionality:

    @allure.title("Переход по клику на «Конструктор»")
    def test_navigate_to_constructor(self, main_page):
        main_page.click_order_feed()
        main_page.click_constructor()
        assert main_page.is_element_displayed(("xpath", BUTTON_CONSTRUCTOR)), (
            "Не удалось перейти в раздел «Конструктор»"
        )

    @allure.title("Переход по клику на «Лента заказов»")
    def test_navigate_to_order_feed(self, main_page):
        main_page.click_order_feed()
        assert "/feed" in main_page.get_current_url(), (
            f"Не удалось перейти в раздел «Лента заказов», текущий URL: {main_page.get_current_url()}"
        )

    @allure.title("Всплывающее окно с деталями ингредиента")
    def test_ingredient_modal(self, main_page):
        main_page.click_ingredient(INGREDIENT_BUN)
        assert main_page.is_element_displayed(("xpath", MODAL_INGREDIENT_DETAILS)), (
            "Не появилось всплывающее окно с деталями ингредиента"
        )

    @allure.title("Закрытие всплывающего окна кликом по крестику")
    def test_close_ingredient_modal(self, main_page):
        main_page.click_ingredient(INGREDIENT_BUN)
        main_page.close_ingredient_modal()
        main_page.wait_for_element_to_disappear(("xpath", MODAL_INGREDIENT_DETAILS))
        assert not main_page.is_element_displayed(("xpath", MODAL_INGREDIENT_DETAILS)), (
            "Всплывающее окно не закрылось"
        )

    @allure.title("Увеличение каунтера ингредиента при добавлении в заказ")
    def test_ingredient_counter_increase(self, main_page):
        main_page.add_ingredient_to_constructor(INGREDIENT_BUN, CONSTRUCTOR_AREA)
        counter = main_page.get_ingredient_counter(COUNTER_BUN)
        assert counter.isdigit() and int(counter) > 0, (
            f"Счетчик ингредиента не увеличился, текущее значение: {counter}"
        )

    @allure.title("Залогиненный пользователь может оформить заказ")
    def test_place_order_authorized(self, main_page, login_page, test_user):
        email, password, token = test_user
        main_page.click_login_button()
        login_page.login(email, password)
        main_page.add_ingredient_to_constructor(INGREDIENT_BUN, CONSTRUCTOR_AREA)
        main_page.click_place_order()
        assert main_page.is_element_displayed(("xpath", "//p[text()='идентификатор заказа']")), (
            "Не удалось оформить заказ"
        )
