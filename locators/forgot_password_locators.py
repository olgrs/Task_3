from selenium.webdriver.common.by import By


EMAIL_INPUT = (By.XPATH, "//input[@name='name']")
BUTTON_RECOVER = (By.XPATH, "//button[text()='Восстановить']")
PASSWORD_INPUT = (By.XPATH, "//input[@name='Введите новый пароль']")
BUTTON_SHOW_PASSWORD = (By.XPATH, "//div[contains(@class, 'input__icon')]")
PASSWORD_FIELD_ACTIVE = (By.XPATH, "//div[contains(@class, 'input_status_active')]")
PAGE_TITLE = (By.XPATH, "//h2[text()='Восстановление пароля']")
