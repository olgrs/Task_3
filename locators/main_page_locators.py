from selenium.webdriver.common.by import By

BURGER_MAKE_HEADING = (By.XPATH, "//h1[text()='Соберите бургер']")

# main buttons
BUTTON_LOGIN_MAIN = (By.XPATH, "//button[text()='Войти в аккаунт']")
BUTTON_PLACE_ORDER = (By.XPATH, "//button[text()='Оформить заказ']")

# ingredients
INGREDIENT_BUN = (By.XPATH, "//p[text()='Краторная булка N-200i']")
CONSTRUCTOR_AREA = (By.XPATH, "//section[contains(@class, 'BurgerConstructor')]")

COUNTER_BUN = (
    By.XPATH,
    "//p[text()='Краторная булка N-200i']/ancestor::div[contains(@class, 'BurgerIngredient')]//p[contains(@class, 'counter__num')]"
)

# modal ingredient
MODAL_INGREDIENT_DETAILS = (By.XPATH, "//div[contains(@class, 'Modal_modal')]")
MODAL_CLOSE_BUTTON = (By.XPATH, "//button[contains(@class, 'Modal_modal__close')]")

# order modal
ORDER_MODAL = (By.XPATH, "//div[contains(@class, 'Modal_modal') and contains(., 'идентификатор заказа')]")
ORDER_NUMBER = (By.XPATH, "//h2[contains(@class, 'Modal_modal__title')]")
ORDER_MODAL_CLOSE = (By.XPATH, "//button[contains(@class, 'Modal_modal__close')]")
