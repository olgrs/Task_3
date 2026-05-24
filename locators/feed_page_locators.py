from selenium.webdriver.common.by import By


ORDER_FEED_HEADING = (By.XPATH, "//h1[text()='Лента заказов']")
ORDER_IN_FEED_LAST = (By.XPATH, "//a[contains(@class, 'OrderHistory_link')]")
ORDER_IN_FEED = (
    By.XPATH, "//ul[contains(@class,'OrderFeed_list')]//p[text()='{}']"
)
ORDER_IN_WORK = (
    By.XPATH,
    "//ul[contains(@class, 'OrderFeed_orderListReady')]//li[contains(., '{}')]"
)
MODAL_ORDER_DETAILS = (By.XPATH, "//div[contains(@class, 'Modal_orderBox')]")
COUNTER_ALL_TIME = (
    By.XPATH,
    "//p[contains(@class, 'OrderFeed_number')][1]"
)
COUNTER_TODAY = (
    By.XPATH,
    "(//p[contains(@class,'OrderFeed_number')])[2]"
)
COUNTER_MAP = {
    "COUNTER_ALL_TIME": COUNTER_ALL_TIME,
    "COUNTER_TODAY": COUNTER_TODAY
}
