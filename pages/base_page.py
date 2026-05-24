import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.base_page_locators import *


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10
        self.wait = WebDriverWait(self.driver, self.timeout)

    # ---------------- NAVIGATION ----------------
    def go_to_url(self, url):
        self.driver.get(url)

    # ------------------ HEADER ------------------
    @allure.step("Клик по кнопке 'Лента Заказов'")
    def click_order_feed(self):
        self.click_to_element(BUTTON_ORDER_FEED)

    @allure.step("Клик по кнопке 'Конструктор'")
    def open_constructor(self):
        self.click_to_element(BUTTON_CONSTRUCTOR)

    @allure.step("Клик по кнопке 'Личный Кабинет'")
    def open_profile(self):
        self.click_to_element(BUTTON_PERSONAL_ACCOUNT)

    # ---------------- ACTIONS ----------------
    def click_to_element(self, locator):
        element = self.find_element_with_wait(locator)

        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            element
        )
        self.wait.until(EC.element_to_be_clickable(locator))
        try:
            element.click()
        except Exception:
            self.driver.execute_script(
                "arguments[0].click();",
                element
            )

    def add_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    def get_text_from_element(self, locator):
        return self.driver.find_element(*locator).text

    def drag_and_drop_element(self, source_locator, target_locator):
        source = self.find_element_with_wait(source_locator)
        target = self.find_element_with_wait(target_locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", source)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", target)
        self.driver.execute_script("""
            function simulateHTML5DragAndDrop(sourceNode, destinationNode) {
                var dataTransfer = new DataTransfer();
                var dragStartEvent = new DragEvent('dragstart', {
                    bubbles: true,
                    cancelable: true,
                    dataTransfer: dataTransfer
                });
                sourceNode.dispatchEvent(dragStartEvent);
                var dropEvent = new DragEvent('drop', {
                    bubbles: true,
                    cancelable: true,
                    dataTransfer: dataTransfer
                });
                destinationNode.dispatchEvent(dropEvent);
                var dragEndEvent = new DragEvent('dragend', {
                    bubbles: true,
                    cancelable: true,
                    dataTransfer: dataTransfer
                });
                sourceNode.dispatchEvent(dragEndEvent);
            }
            simulateHTML5DragAndDrop(arguments[0], arguments[1]);
        """, source, target)

    # ---------------- STATE CHECKS ----------------
    def is_element_displayed(self, locator):
        try:
            return self.driver.find_element(*locator).is_displayed()
        except Exception:
            return False

    # ---------------- WAITS ----------------
    def wait_for_element_to_be_visible(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_for_element_to_be_clickable(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    def wait_for_url_to_be(self, url, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.url_to_be(url)
        )

    def wait_for_url_contains(self, partial_url, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.url_contains(partial_url)
        )

    def wait_for_element_to_disappear(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.invisibility_of_element_located(locator)
        )

    def wait_counter_increases(self, locator, old_value, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            lambda d: (
                (el := d.find_elements(*locator))
                and el[0].text.strip().isdigit()
                and int(el[0].text) > old_value
            )
        )

    # ---------------- UTILS ----------------
    def refresh(self):
        self.driver.refresh()

    def scroll_to(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def find_element_with_wait(self, locator):
        self.wait.until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def find_elements_with_wait(self, locator):
        self.wait.until(EC.visibility_of_element_located(locator))
        return self.driver.find_elements(*locator)

    def get_current_url(self):
        return self.driver.current_url
