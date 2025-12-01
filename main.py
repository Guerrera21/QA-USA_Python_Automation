import data
import helpers

class TestUrbanRoutes:
    @classmethod
    def setup_class(cls):
        #check if the Urban Routes server is reachable
        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print("Connected to Urban Routes server")
        else:
            print("Cannot connect to Urban Routes. Check the server is still on and still running.")

    def test_set_route(self):
        # Add in s8
        print("function created for set route")
        pass
    def test_select_plan(self):
        # Add in s8
        print("function created for select plan")
        pass
    def test_fill_phone_number(self):
        # Add in s8
        print("function created for fill phone number")
        pass
    def test_fill_card(self):
        # Add in s8
        print("function created for fill card")
        pass
    def test_comment_for_driver(self):
        # Add s8
        print("function created for comment for driver")
        pass
    def test_order_2_ice_cream(self):
        # Looping twice for ordering 2 ice creams
        for _ in range (2):
            # Add in s8
            pass
    def test_car_search_model_appears(self):
        # Add in s8
        print("function created for car search model")
        pass

    print('test1')