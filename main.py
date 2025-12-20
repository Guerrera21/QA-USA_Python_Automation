from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.devtools.v141.fed_cm import click_dialog_button

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
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome(desired_capabilities=capabilities)

    @classmethod
    def test_set_route(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page = UrbanRoutesPage(self.driver)
        page.enter_from(data.ADDRESS_FROM)
        page.enter_to(data.ADDRESS_TO)

    def test_select_plan(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page = UrbanRoutesPage(self.driver)
        page.click_call_a_taxi(data.CALL_A_TAXI)
        page.click_supportive_button(data.SUPPORTIVE_BUTTON)

    def test_fill_phone_number(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page = UrbanRoutesPage(self.driver)
        page.enter_phone_number(data.PHONE_NUMBER)

    def test_fill_card(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page = UrbanRoutesPage(self.driver)
        page.test_fill_card(
            data.CARD_NUMBER,
            data.CARD_CODE
        )

    def test_comment_for_driver(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page = UrbanRoutesPage(self.driver)
        page.comment_for_driver(data.COMMENT)

    def test_order_blanket_handkerchiefs(self):
       self.driver.get(data.URBAN_ROUTES_URL)
       page = UrbanRoutesPage(self.driver)
       page.order_blanket_handkerchiefs(data.order_blanket_handerkerchiefs)

    def test_order_2_ice_cream(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page = UrbanRoutesPage(self.driver)
        page.order_2_ice_creams(data.ORDER_2_ICE_CREAMS)

    def test_car_search_modal_appears(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        page = UrbanRoutesPage(self.driver)
        page.test_car_search_modal_appears(data.car_search_modal_appears)
