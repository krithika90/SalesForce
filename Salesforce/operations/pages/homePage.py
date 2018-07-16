from bases.base_setup import BaseSetup
from bases.driver_element import DriverElements
from tests import map_driver_element


class HomePage(BaseSetup, DriverElements):

    def __init__(self, driver):
        driverele = DriverElements(driver)
        self.driver = driver

    def verify_header(self):
        self.sleep_time(30)
        boolean = self.element_is_visible(map_driver_element.home_page.get('headerByXpath'), "xpath")
        return boolean

    def verify_page_title(self):
        boolean = ''
        element = self.get_element(map_driver_element.home_page.get('pageTitleByXpath'), "xpath")
        if element.get_attribute('text') == "Home | Salesforce":
            boolean = True
        return boolean
