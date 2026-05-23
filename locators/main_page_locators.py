# Кнопки в хедере
BUTTON_CONSTRUCTOR = "//p[text()='Конструктор']"
BUTTON_ORDER_FEED = "//p[text()='Лента Заказов']"
BUTTON_PERSONAL_ACCOUNT = "//p[text()='Личный Кабинет']"

# Кнопки на главной
BUTTON_LOGIN_MAIN = "//button[text()='Войти в аккаунт']"
BUTTON_PLACE_ORDER = "//button[text()='Оформить заказ']"

# Конструктор бургера
INGREDIENT_BUN = "//p[text()='Краторная булка N-200i']"
INGREDIENT_SAUCE = "//p[text()='Соус Spicy-X']"
INGREDIENT_FILLING = "//p[text()='Мясо бессмертных моллюсков Protostomia']"
CONSTRUCTOR_AREA = "//section[contains(@class, 'BurgerConstructor')]"

# Счетчики ингредиентов
COUNTER_BUN = "//p[text()='Краторная булка N-200i']/ancestor::div[contains(@class, 'BurgerIngredient')]//p[contains(@class, 'counter__num')]"

# Модальное окно ингредиента
MODAL_INGREDIENT_DETAILS = "//div[contains(@class, 'Modal_modal')]"
MODAL_INGREDIENT_TITLE = "//h2[contains(@class, 'Modal_modal__title')]"
MODAL_CLOSE_BUTTON = "//button[contains(@class, 'Modal_modal__close')]"

# Модальное окно подтверждения заказа
ORDER_MODAL = "//div[contains(@class, 'Modal_modal') and contains(., 'идентификатор заказа')]"
ORDER_NUMBER = "//h2[contains(@class, 'Modal_modal__title')]"
ORDER_MODAL_CLOSE = "//button[contains(@class, 'Modal_modal__close')]"