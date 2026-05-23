import allure
from locators.main_page_locators import *
from locators.feed_page_locators import *


class TestOrderFeed:

    @allure.title("Открытие всплывающего окна с деталями заказа при клике на заказ в ленте")
    def test_order_modal_in_feed(self, main_page, feed_page):
        main_page.click_order_feed()
        feed_page.wait_for_first_order()   # нужно добавить метод в FeedPage
        feed_page.click_first_order()
        assert feed_page.is_element_displayed(("xpath", MODAL_ORDER_DETAILS)), (
            "Не открылось всплывающее окно с деталями заказа"
        )

    @allure.title("Заказы пользователя из «Истории заказов» отображаются на странице «Лента заказов»")
    def test_user_order_in_feed(self, main_page, login_page, feed_page, test_user):
        email, password, token = test_user
        main_page.click_login_button()
        login_page.login(email, password)

        main_page.add_ingredient_to_constructor(INGREDIENT_BUN, CONSTRUCTOR_AREA)
        main_page.click_place_order()
        order_number = main_page.get_order_number()
        main_page.close_order_modal()

        main_page.click_order_feed()
        feed_page.wait_for_order_number(order_number)   # нужно добавить метод
        assert feed_page.is_element_displayed(("xpath", f"//p[contains(text(), '{order_number}')]")), (
            f"Заказ с номером {order_number} не найден в ленте заказов"
        )

    @allure.title("При создании нового заказа увеличиваются счетчики «Выполнено за всё время» и «Выполнено за сегодня»")
    def test_counters_increase(self, main_page, login_page, feed_page, test_user):
        email, password, token = test_user
        main_page.click_order_feed()
        feed_page.wait_for_counters()
        old_all_time = feed_page.get_counter_all_time()
        old_today = feed_page.get_counter_today()

        main_page.click_constructor()
        main_page.click_login_button()
        login_page.login(email, password)

        main_page.add_ingredient_to_constructor(INGREDIENT_BUN, CONSTRUCTOR_AREA)
        main_page.click_place_order()
        order_number = main_page.get_order_number()
        main_page.close_order_modal()

        main_page.click_order_feed()
        feed_page.wait_for_order_in_work(order_number)

        new_all_time = feed_page.get_counter_all_time()
        new_today = feed_page.get_counter_today()

        assert int(new_all_time) > int(old_all_time), (
            f"Счетчик «Выполнено за всё время» не увеличился: было {old_all_time}, стало {new_all_time}"
        )
        assert int(new_today) > int(old_today), (
            f"Счетчик «Выполнено за сегодня» не увеличился: было {old_today}, стало {new_today}"
        )

    @allure.title("После оформления заказа его номер появляется в разделе «В работе»")
    def test_order_appears_in_work(self, main_page, login_page, feed_page, test_user):
        email, password, token = test_user
        main_page.click_login_button()
        login_page.login(email, password)

        main_page.add_ingredient_to_constructor(INGREDIENT_BUN, CONSTRUCTOR_AREA)
        main_page.click_place_order()
        order_number = main_page.get_order_number()
        main_page.close_order_modal()

        main_page.click_order_feed()
        feed_page.wait_for_order_in_work(order_number)
        assert order_number in feed_page.get_order_in_work(), (
            f"Номер заказа {order_number} не появился в разделе «В работе»"
        )
