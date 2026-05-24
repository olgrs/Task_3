from selenium.webdriver.common.by import By


BUTTON_PROFILE = (By.XPATH, "//a[text()='Профиль']")
BUTTON_ORDER_HISTORY = (By.XPATH, "//a[text()='История заказов']")
BUTTON_LOGOUT = (By.XPATH, "//button[text()='Выход']")

TEXT_PROFILE = (By.XPATH, "//p[text()='В этом разделе вы можете изменить свои персональные данные']")
ORDER_HISTORY_LAST_NUMBER = (
    By.XPATH,
    "(//a[contains(@class, 'OrderHistory_link')]//p[contains(@class, 'text_type_digits-default')])[1]"
)
ORDER_HISTORY_LIST = (By.XPATH, "//a[contains(@class, 'Account_link_active')]")
