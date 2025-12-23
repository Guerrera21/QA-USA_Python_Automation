from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import helpers


class UrbanRoutesPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    FROM_FIELD = (By.ID, "from")
    TO_FIELD = (By.ID, "to")
    CALL_A_TAXI = (By.XPATH, '//button[text()="Call a taxi"]')
    SUPPORTIVE_BUTTON = (By.XPATH, '//img[@alt="Supportive"]')
    ACTIVE_PLAN = (By.CSS_SELECTOR, '.tcard.active .tcard-title')
    ENTER_PHONE_NUMBER = (By.XPATH, '//div[text()="Phone number"]')
    CLICK_NEXT_BUTTON = (By.XPATH, "//button[text()='Next']")
    WRITE_CODE = (By.XPATH, "//input[@id='code']")
    RETRIEVE_PHONE_CODE = (By.XPATH, "//label[@for='code']")
    CLICK_CONFIRM_BUTTON = (By.CSS_SELECTOR, "css=button[type='submit']")
    FILL_CARD = (By.XPATH, '//div[text()="Add card"]')
    CARD_NUMBER = (By.XPATH, "//div[@class='pp-title']")
    CARD_CODE = (By.XPATH, "//input[@id='code']")
    COMMENT_TO_DRIVER = (By.XPATH, '//label[text()="Message to the driver..."]')
    ORDER_2_ICE_CREAM = (By.XPATH, "//div[text()='2']")
    BLANKET_HANDERKERCHIEFS = (By.XPATH, "//span[@class='slider round']")
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

    def click_next_button(self):
        self.driver.find_element(*self.CLICK_NEXT_BUTTON).click()

    def retrieve_phone_code(self):
        code = helpers.retrieve_phone_code(self.driver)

    def write_code(self, code):
        self.driver.find_element(*self.WRITE_CODE).send_keys(code)

    def click_confirm_button(self):
        self.driver.find_element(*self.CLICK_CONFIRM_BUTTON).click()

    def test_fill_card(self, card_number, card_code):
        self.driver.find_element(*self.CARD_NUMBER).send_keys(card_number)
        self.driver.find_element(*self.CARD_CODE).send_keys(card_code)

    def comment_for_driver(self, message):
        self.driver.find_element(*self.COMMENT_TO_DRIVER).send_keys(message)

    def order_blanket_handerkerchiefs(self):
        self.driver.find_element(*self.BLANKET_HANDERKERCHIEFS).click()

    def test_order_2_ice_cream(self):
        self.driver.find_element(*self.ORDER_2_ICE_CREAM).click()

    def car_search_modal(self):
        self.driver.find_element(*self.CAR_SEARCH_MODAL).click()

    def get_from(self):
        return self.driver.find_element(*self.FROM_FIELD).get_attribute("value")
    def get_to(self):
        return self.driver.find_element(*self.TO_FIELD).get_attribute("value")

    def get_active_plan(self):
        return self.driver.find_element(*self.ACTIVE_PLAN).text

    def get_phone_number(self):
        return self.driver.find_element(*self.ENTER_PHONE_NUMBER).text

    def get_card_code(self):
        return self.driver.find_element(*self.CARD_CODE).text

    def get_comment_to_driver(self):
        return self.driver.find_element(*self.COMMENT_TO_DRIVER).text

    def order_2_ice_cream(self):
        return self.driver.find_element(*self.ORDER_2_ICE_CREAM).click()

    def blanket_handkerchiefs(self):
        return self.driver.find_element(*self.BLANKET_HANDERKERCHIEFS).click()

    def car_search_modal(self):
        return self.driver.find_element(*self.CAR_SEARCH_MODAL).click()


