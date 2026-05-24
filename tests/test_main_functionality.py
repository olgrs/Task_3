import allure


class TestMainFunctionality:
    @allure.title("Переход по клику на 'Конструктор'")
    def test_constructor_navigation(self, main_page):
        main_page.open_constructor()
        assert main_page.is_constructor_displayed(), (
            "Не удалось перейти в раздел «Конструктор»"
        )

    @allure.title("Переход по клику на 'Ленту Заказов'")
    def test_feed_navigation(self, main_page, feed_page):
        main_page.click_order_feed()
        assert feed_page.is_feed_displayed(), (
            "Не удалось перейти в раздел «Лента Заказов»"
        )

    @allure.title("Всплывающее окно с деталями ингредиента")
    def test_ingredient_modal(self, main_page):
        main_page.open_ingredient()
        assert main_page.is_ingredient_modal_open(), (
            "Не появилось всплывающее окно с деталями ингредиента"
        )

    @allure.title("Закрытие всплывающего окна кликом по крестику")
    def test_close_modal(self, main_page):
        main_page.open_ingredient()
        main_page.close_ingredient_modal()
        assert main_page.is_ingredient_modal_closed(), (
            "Всплывающее окно не закрылось"
        )

    @allure.title("Увеличение каунтера ингредиента при добавлении в заказ")
    def test_counter_increase(self, main_page):
        counter = main_page.create_bun_burger()
        assert int(counter) > 0, (
            f"Счетчик ингредиента не увеличился, текущее значение: {counter}"
        )

    @allure.title("Залогиненный пользователь может оформить заказ")
    def test_create_order(self, main_page, logged_in_user):
        main_page.create_order()
        assert main_page.is_order_modal_displayed(), (
            "Не удалось оформить заказ"
        )
