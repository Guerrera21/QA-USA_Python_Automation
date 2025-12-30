from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import helpers
from data import CARD_NUMBER


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
    PHONE_NUMBER = (By.ID, "phone")
    GET_PHONE_NUMBER = (By.CLASS_NAME, 'np-text')
    CLICK_NEXT_BUTTON = (By.XPATH, "//button[text()='Next']")
    WRITE_CODE = (By.XPATH, "//input[@id='code']")
    RETRIEVE_PHONE_CODE = (By.XPATH, "//label[@for='code']")
    CLICK_CONFIRM_BUTTON = (By.XPATH, "//button[contains(text(), 'Confirm')]")
    PAYMENT_METHOD = (By.CLASS_NAME, "pp-value-text")
    ADD_CARD = (By.CLASS_NAME, "pp-plus")
    CARD_NUMBER = (By.CLASS_NAME, "card-input")
    CARD_CODE = (By.CSS_SELECTOR, "#code.card-input")
    GET_CARD_NUMBER = (By.ID, "number")
    GET_CODE = (By.NAME, "code")
    LINK_BUTTON = (By.XPATH, "//button[text()='Link']")
    COMMENT_TO_DRIVER = (By.ID, "comment")
    BLANKET_HANDKERCHIEFS = (By.CLASS_NAME, "r-sw")
    BLANKET_CHECKBOX = (By.XPATH, "//input[@type='checkbox']")
    PLUS_ICON_LOCATOR = (By. XPATH, '(//div[@class="counter-plus"])[1]')
    GET_2_ICE_CREAM = (By. XPATH, '(//div[@class="counter-value"])[1]')
    CAR_SEARCH_MODAL = (By.CSS_SELECTOR, '.smart-button-main')
    GET_MODAL = (By.CLASS_NAME, "smart-button-secondary")

    def enter_from(self, address):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(self.FROM_FIELD))
        self.driver.find_element(*self.FROM_FIELD).send_keys(address)

    def enter_to(self, address):
        self.driver.find_element(*self.TO_FIELD).send_keys(address)

    def click_call_a_taxi(self):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(self.CALL_A_TAXI))
        self.driver.find_element(*self.CALL_A_TAXI).click()

    def click_supportive_button(self):
        self.driver.find_element(*self.SUPPORTIVE_BUTTON).click()

    def enter_phone_number(self, phone_number):
        self.driver.find_element(*self.ENTER_PHONE_NUMBER).click()
        self.driver.find_element(*self.PHONE_NUMBER).send_keys(phone_number)

    def phone_number(self, phone_number):
        WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(self.PHONE_NUMBER))
        self.driver.find_element(*self.PHONE_NUMBER).click()

    def click_next_button(self):
        self.driver.find_element(*self.CLICK_NEXT_BUTTON).click()

    def retrieve_phone_code(self):
        code = helpers.retrieve_phone_code(self.driver)

    def write_code(self, code):
        self.driver.find_element(*self.WRITE_CODE).send_keys(code)

    def click_confirm_button(self):
        self.driver.find_element(*self.CLICK_CONFIRM_BUTTON).click()

    def payment_method(self):
        self.driver.find_element(*self.PAYMENT_METHOD).click()

    def add_card(self):
        self.driver.find_element(*self.ADD_CARD).click()

    def fill_card(self, card_number, card_code):
        self.driver.find_element(*self.CARD_NUMBER).send_keys(card_number)
        self.driver.find_element(*self.CARD_CODE).send_keys(card_code)

    def link_button(self):
        self.driver.find_element(*self.CARD_CODE).send_keys(Keys.TAB)
        WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(self.LINK_BUTTON))
        self.driver.find_element(*self.LINK_BUTTON).click()

    def comment_to_driver(self, message):
        self.driver.find_element(*self.COMMENT_TO_DRIVER).send_keys(message)

    def blanket_handkerchiefs(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.BLANKET_HANDKERCHIEFS))
        self.driver.find_element(*self.BLANKET_HANDKERCHIEFS).click()

    def get_blanket_checkbox(self):
        return self.driver.find_element(*self.BLANKET_CHECKBOX).is_selected()

    def order_2_ice_cream(self):
        number_of_ice_cream = 2
        for i in range(number_of_ice_cream):
            self.driver.find_element(*self.PLUS_ICON_LOCATOR).click()

    def car_search_modal(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.CAR_SEARCH_MODAL)).click()
        self.driver.find_element(*self.CAR_SEARCH_MODAL).click()

    def get_from(self):
        return self.driver.find_element(*self.FROM_FIELD).get_attribute("value")
    def get_to(self):
        return self.driver.find_element(*self.TO_FIELD).get_attribute("value")

    def get_active_plan(self):
        return self.driver.find_element(*self.ACTIVE_PLAN).text

    def get_phone_number(self):
        return self.driver.find_element(*self.GET_PHONE_NUMBER).text

    def get_fill_card(self):
        return self.driver.find_element(*self.PAYMENT_METHOD).text

    def get_comment_to_driver(self):
        return self.driver.find_element(*self.COMMENT_TO_DRIVER).get_attribute('value')

    def get_2_ice_cream(self):
        return self.driver.find_element(*self.GET_2_ICE_CREAM).text

    def get_modal(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.CAR_SEARCH_MODAL))
        return self.driver.find_element(*self.GET_MODAL)


