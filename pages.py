from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class UrbanRoutesPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    FROM_FIELD = (By.ID, "from")
    TO_FIELD = (By.ID, "to")
    CALL_A_TAXI = (By.XPATH, '//button[text()="Call a taxi"]')
    SUPPORTIVE_BUTTON = (By.XPATH, '//img[@alt="Supportive"]')
    ENTER_PHONE_NUMBER = (By.XPATH, '//div[text()="Phone number"]')
    CASH_PAYMENT = (By.XPATH, '//div[text()="Cash"]')
    FILL_CARD = (By.XPATH, '//div[text()="Add card"]')
    COMMENT_TO_DRIVER = (By.XPATH, '//label[text()="Message to the driver..."]')
    ORDER_ICE_CREAM = (By.XPATH, '//div[text()="Ice cream"]')
    CAR_SEARCH_MODAL = (By.XPATH, '//span[text()="The route will be 1 km. and will take 2 min."]')

    def enter_from(self, address):
        self.driver.find_element(*self.FROM_FIELD).send_keys(address)

    def enter_to(self, address):
        self.driver.find_element(*self.TO_FIELD).send_keys(address)

    def click_call_a_taxi(self):
        self.driver.find_element(*self.CALL_A_TAXI).click()

    def click_supportive_button(self):
        self.driver.find_element(*self.SUPPORTIVE_BUTTON).click()

    def enter_phone_number(self, phone_number):
        self.driver.find_element(*self.ENTER_PHONE_NUMBER).send_keys(phone_number)

    def test_fill_card(self):
        self.driver.find_element(*self.CARD_NUMBER).send_keys()
        self.driver.find_element(*self.CARD_CARD).send_keys()

    def cash_payment(self, amount):
        self.driver.find_element(*self.CASH_PAYMENT).click()

    def comment_for_driver(self):
        self.driver.find_element(*self.COMMENT_FOR_DRIVER).send_keys(COMMENT)

    def order_blanket_handerkerchiefs(self):
        self.driver.find_element(*self.order_blanket_handerkerchiefs).click()

    def test_order_2_ice_cream(self):
        self.driver.find_element(*self.test_order_2_ice_cream)

    def test_car_search_modal_appears(self):
        self.driver.find_element(*self.test_car_search_modal_appears)