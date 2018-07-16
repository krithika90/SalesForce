from bases.base_setup import BaseSetup
from bases.driver_element import DriverElements
from tests import map_driver_element
from tests import user_details
from pages.gmailPage import GmailPage

class LoginPage(BaseSetup, DriverElements):

    def __init__(self, driver):
        driverele = DriverElements(driver)
        self.driver = driver

    def salesforce_logo(self):
        self.sleep_time(15)
        bool_value = self.element_is_visible(map_driver_element.login_page.get('logoByXpath'), "xpath")
        return bool_value

    def username_login(self):
        self.sleep_time(7)
        self.send_keys_to_element(map_driver_element.login_page.get('usernameByID'), "id",
                                  user_details.login_details.get('username'))

    def password_login(self):
        self.send_keys_to_element(map_driver_element.login_page.get('passwordByID'), "id",
                                  user_details.login_details.get('password'))

    def login(self):
        self.click_on_element(map_driver_element.login_page.get('loginButtonById'), "id")

    def signup_link(self):
        self.click_on_element(map_driver_element.login_page.get('tryForFreelinkByID'), "id")

    def verification_code(self, code):
        self.sleep_time(5)
        self.send_keys_to_element(map_driver_element.login_page.
                                  get('verificationCodeByXpath'), "xpath", code)
        self.click_on_element(map_driver_element.login_page.get('verifyButtonByXpath'), "xpath")




