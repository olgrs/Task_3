from selenium.common.exceptions import (
    TimeoutException,
    ElementClickInterceptedException
)
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10
        self.wait = WebDriverWait(self.driver, self.timeout)

    def go_to_url(self, url):
        self.driver.get(url)

    def find_element_with_wait(self, locator):
        self.wait.until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)
    
    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    def click_to_element(self, locator):
        try:
            self.wait.until(EC.element_to_be_clickable(locator))
            self.driver.find_element(*locator).click()
        except (TimeoutException, ElementClickInterceptedException):
            element = self.driver.find_element(*locator)
            self.driver.execute_script("arguments[0].click();", element)

    def add_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)

    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text

    def scroll_to_element(self, locator):
        element = self.find_element_with_wait(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def get_current_url(self):
        return self.driver.current_url

    def switch_to_another_window(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    def wait_for_url_not_blank(self):
        WebDriverWait(self.driver, 10).until(lambda d: d.current_url != "about:blank")

    def close_cookie_window(self, locator):
        self.find_element_with_wait(locator)
        self.click_to_element(locator)

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

    def wait_for_url_to_be(self, url, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.url_to_be(url))

    def wait_for_element_to_disappear(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    def is_element_displayed(self, locator):
        try:
            element = self.driver.find_element(*locator)
            return element.is_displayed()
        except (TimeoutException, ElementClickInterceptedException):
            return False

    def wait_for_element_present(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def wait_for_text_in_element(self, locator, text, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.text_to_be_present_in_element(locator, text))

    def wait_for_url_contains(self, partial_url, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.url_contains(partial_url))

    def refresh_page(self):
        self.driver.refresh()

    def wait_for_element_visible(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
