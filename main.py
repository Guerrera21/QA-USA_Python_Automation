from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v141.fed_cm import click_dialog_button
from selenium.webdriver.support.wait import WebDriverWait

import data
import helpers
from pages import UrbanRoutesPage


class TestUrbanRoutes:
    @classmethod
    def setup_class(cls):
        #check if the Urban Routes server is reachable
        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print("Connected to Urban Routes server")
        else:
            print("Cannot connect to Urban Routes. Check the server is still on and still running.")

        # do not modify - we need additional logging enabled in order to retrieve phone confirmation code
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()

    def test_set_route(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page = UrbanRoutesPage(self.driver)
        page.enter_from(data.ADDRESS_FROM)
        page.enter_to(data.ADDRESS_TO)
        assert page.get_from() == data.ADDRESS_FROM
        assert page.get_to() == data.ADDRESS_TO

    def test_select_plan(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page = UrbanRoutesPage(self.driver)
        page.enter_from(data.ADDRESS_FROM)
        page.enter_to(data.ADDRESS_TO)
        page.click_call_a_taxi()
        page.click_supportive_button()
        assert page.get_active_plan()=="Supportive"


    def test_fill_phone_number(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page = UrbanRoutesPage(self.driver)
        page.enter_from(data.ADDRESS_FROM)
        page.enter_to(data.ADDRESS_TO)
        page.click_call_a_taxi()
        page.enter_phone_number()
        page.click_next_button()
        page.write_code(helpers.retrieve_phone_code(self.driver))
        page.CLICK_CONFIRM_BUTTON()
        assert page.get_PHONE_NUMBER()== data.PHONE_NUMBER

    def test_fill_card(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page = UrbanRoutesPage(self.driver)
        page.enter_from(data.ADDRESS_FROM)
        page.enter_to(data.ADDRESS_TO)
        page.click_call_a_taxi()
        # 1. Select the 'Card' option
        card_option = self.driver.find_element(By.CSS_SELECTOR, "label[for='card-1']")
        card_option.click()
        # 2. Fill in the 'Add Card' form (if visible)
        card_num_field = self.driver.find_element(By.ID, "number")
        card_num_field.send_keys("1234567812345678")
        cvc_field = self.driver.find_element(By.ID, "code")
        cvc_field.send_keys("123")
        # 3. Wait for the Link button to be enabled, then click
        link_button = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Link']"))
        )
        link_button.click()
        assert page.FILL_CARD() == "CARD"

    def test_comment_for_driver(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page = UrbanRoutesPage(self.driver)
        page.enter_from(data.ADDRESS_FROM)
        page.enter_to(data.ADDRESS_TO)
        page.click_call_a_taxi()
        page.click_supportive_button()
        page.COMMENT_TO_DRIVER("stop at the juice bar, please")
        assert page.get_comment_to_driver() == 'message'

    def test_order_blanket_handkerchiefs(self):
       self.driver.get(data.URBAN_ROUTES_URL)
       page = UrbanRoutesPage(self.driver)
       page.enter_from(data.ADDRESS_FROM)
       page.enter_to(data.ADDRESS_TO)
       page.click_call_a_taxi()
       page.click_supportive_button()
       page.order_blanket_handerkerchiefs()
       assert page.get_blanket_handerkerchiefs()

    def test_order_2_ice_cream(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page = UrbanRoutesPage(self.driver)
        page.enter_from(data.ADDRESS_FROM)
        page.enter_to(data.ADDRESS_TO)
        page.click_call_a_taxi()
        page.click_supportive_button()
        assert page.get_order_2_ice_cream()=='order 2 ice cream'

    def test_car_search_modal_appears(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page = UrbanRoutesPage(self.driver)
        page.enter_from(data.ADDRESS_FROM)
        page.enter_to(data.ADDRESS_TO)
        page.click_call_a_taxi()
        page.click_supportive_button()
        page.car_search_modal()
        assert page.get_car_search_modal().is_displayed()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()