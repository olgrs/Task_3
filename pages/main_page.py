import allure

from data import BASE_URL
from locators.main_page_locators import *
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step("Открыть главную страницу")
    def open(self):
        self.go_to_url(BASE_URL)

    @allure.step("Клик по кнопке 'Войти в аккаунт'")
    def click_login_button(self):
        self.click_to_element(BUTTON_LOGIN_MAIN)

    @allure.step("Проверка отображения конструктора")
    def is_constructor_displayed(self):
        return self.is_element_displayed(BURGER_MAKE_HEADING)

    @allure.step("Проверка отображения модального окна")
    def is_order_modal_displayed(self):
        return self.is_element_displayed(ORDER_MODAL)
    
    @allure.step("Создание заказа и получение номера")
    def create_order(self):
        self.add_ingredient_to_constructor(INGREDIENT_BUN, CONSTRUCTOR_AREA)
        self.click_to_element(BUTTON_PLACE_ORDER)
        self.wait.until(
            lambda _: (
                self.get_text_from_element(ORDER_NUMBER).strip().isdigit()
                and self.get_text_from_element(ORDER_NUMBER).strip() != "9999"
            )
        )
        return self.get_text_from_element(ORDER_NUMBER)

    @allure.step("Добавить ингредиент в конструктор")
    def add_ingredient_to_constructor(self, ingredient_locator, constructor_locator):
        self.drag_and_drop_element(ingredient_locator, constructor_locator)

    @allure.step("Создание заказа с булочкой")
    def create_bun_burger(self):
        self.add_ingredient_to_constructor(
            INGREDIENT_BUN, CONSTRUCTOR_AREA
        )
        return self.get_text_from_element(COUNTER_BUN)

    @allure.step("Закрыть модальное окно подтверждения заказа")
    def close_order_modal(self):
        self.click_to_element((ORDER_MODAL_CLOSE))

    @allure.step("Клик по ингредиенту")
    def open_ingredient(self):
        self.click_to_element(INGREDIENT_BUN)

    @allure.step("Закрыть окно описания ингредиента")
    def close_ingredient_modal(self):
        self.click_to_element(MODAL_CLOSE_BUTTON)

    @allure.step("Отображение окна описания ингредиента")
    def is_ingredient_modal_open(self):
        return self.is_element_displayed(MODAL_INGREDIENT_DETAILS)

    @allure.step("Проверка закрытия окна описания ингредиента")
    def is_ingredient_modal_closed(self):
        self.wait_for_element_to_disappear(MODAL_INGREDIENT_DETAILS)
        return True
