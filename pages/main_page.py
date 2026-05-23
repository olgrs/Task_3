import allure
from pages.base_page import BasePage
from locators.main_page_locators import *
from data import BASE_URL


class MainPage(BasePage):

    @allure.step("Открыть главную страницу")
    def open(self):
        self.go_to_url(BASE_URL)

    @allure.step("Клик по кнопке 'Конструктор'")
    def click_constructor(self):
        self.click_to_element(("xpath", BUTTON_CONSTRUCTOR))

    @allure.step("Клик по кнопке 'Лента Заказов'")
    def click_order_feed(self):
        self.click_to_element(("xpath", BUTTON_ORDER_FEED))

    @allure.step("Клик по кнопке 'Личный Кабинет'")
    def click_personal_account(self):
        self.click_to_element(("xpath", BUTTON_PERSONAL_ACCOUNT))

    @allure.step("Клик по кнопке 'Войти в аккаунт'")
    def click_login_button(self):
        self.click_to_element(("xpath", BUTTON_LOGIN_MAIN))

    @allure.step("Клик по ингредиенту")
    def click_ingredient(self, ingredient_locator):
        self.scroll_to_element(("xpath", ingredient_locator))
        self.click_to_element(("xpath", ingredient_locator))

    @allure.step("Получить текст заголовка модального окна ингредиента")
    def get_ingredient_modal_title(self):
        return self.get_text_from_element(("xpath", MODAL_INGREDIENT_TITLE))

    @allure.step("Закрыть модальное окно ингредиента")
    def close_ingredient_modal(self):
        self.click_to_element(("xpath", MODAL_CLOSE_BUTTON))

    @allure.step("Получить счетчик ингредиента")
    def get_ingredient_counter(self, counter_locator):
        return self.get_text_from_element(("xpath", counter_locator))

    @allure.step("Клик по кнопке 'Оформить заказ'")
    def click_place_order(self):
        self.click_to_element(("xpath", BUTTON_PLACE_ORDER))

    @allure.step("Получить номер заказа из модального окна")
    def get_order_number(self):
        return self.get_text_from_element(("xpath", ORDER_NUMBER))

    @allure.step("Закрыть модальное окно подтверждения заказа")
    def close_order_modal(self):
        self.click_to_element(("xpath", ORDER_MODAL_CLOSE))

    @allure.step("Добавить ингредиент в конструктор (drag-and-drop)")
    def add_ingredient_to_constructor(self, ingredient_locator, constructor_locator):
        self.drag_and_drop_element(("xpath", ingredient_locator), ("xpath", constructor_locator))
