import time

from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v141.fed_cm import click_dialog_button
from selenium.webdriver.support.wait import WebDriverWait

import data
import helpers
from data import CARD_NUMBER
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
        page.enter_phone_number(data.PHONE_NUMBER)
        page.click_next_button()
        page.write_code(helpers.retrieve_phone_code(self.driver))
        page.click_confirm_button()
        assert page.get_phone_number()== data.PHONE_NUMBER

    def test_fill_card(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page = UrbanRoutesPage(self.driver)
        page.enter_from(data.ADDRESS_FROM)
        page.enter_to(data.ADDRESS_TO)
        page.click_call_a_taxi()
        page.click_supportive_button()
        page.payment_method()
        page.add_card()
        page.fill_card(data.CARD_NUMBER, data.CARD_CODE)
        page.link_button()
        assert page.get_fill_card() == 'Card'

    def test_comment_to_driver(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page = UrbanRoutesPage(self.driver)
        page.enter_from(data.ADDRESS_FROM)
        page.enter_to(data.ADDRESS_TO)
        page.click_call_a_taxi()
        page.comment_to_driver(data.MESSAGE_FOR_DRIVER)
        assert page.get_comment_to_driver()== data.MESSAGE_FOR_DRIVER

    def test_order_blanket_handkerchiefs(self):
       self.driver.get(data.URBAN_ROUTES_URL)
       page = UrbanRoutesPage(self.driver)
       page.enter_from(data.ADDRESS_FROM)
       page.enter_to(data.ADDRESS_TO)
       page.click_call_a_taxi()
       page.click_supportive_button()
       page.blanket_handkerchiefs()
       assert page.get_blanket_checkbox()

    def test_order_2_ice_cream(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page = UrbanRoutesPage(self.driver)
        page.enter_from(data.ADDRESS_FROM)
        page.enter_to(data.ADDRESS_TO)
        page.click_call_a_taxi()
        page.click_supportive_button()
        page.order_2_ice_cream()
        assert page.get_2_ice_cream() == '2'

    def test_car_search_modal_appears(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page = UrbanRoutesPage(self.driver)
        page.enter_from(data.ADDRESS_FROM)
        page.enter_to(data.ADDRESS_TO)
        page.click_call_a_taxi()
        page.click_supportive_button()
        page.car_search_modal()
        assert page.get_modal().is_displayed()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()