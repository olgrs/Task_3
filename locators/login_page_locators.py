from selenium.webdriver.common.by import By


EMAIL_INPUT = (By.XPATH, "//input[@name='name']")
PASSWORD_INPUT = (By.XPATH, "//input[@name='Пароль']")
BUTTON_LOGIN = (By.XPATH, "//button[text()='Войти']")
BUTTON_FORGOT_PASSWORD = (By.XPATH, "//a[text()='Восстановить пароль']")
