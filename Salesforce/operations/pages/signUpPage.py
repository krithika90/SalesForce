from bases.base_setup import BaseSetup
from bases.driver_element import DriverElements
from tests import map_driver_element, user_details
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


class SignUpPage(BaseSetup, DriverElements):

    def __init__(self, driver):
        driverele = DriverElements(driver)
        self.driver = driver

    def enter_firstName(self):
        self.sleep_time(7)
        self.send_keys_to_element(map_driver_element.signup_page.get('firstNameByID'), "id",
                                  user_details.new_user_details.get('firstName'))

    def enter_lastName(self):
        self.send_keys_to_element(map_driver_element.signup_page.get('lastNameByID'), "id",
                                  user_details.new_user_details.get('lastName'))

    def enter_jobTitle(self):
        self.get_element(map_driver_element.signup_page.get('lastNameByID'), "id").\
            send_keys(Keys.TAB, Keys.ENTER, Keys.ARROW_DOWN, Keys.ENTER)

    def enter_email(self):
        self.send_keys_to_element(map_driver_element.signup_page.get('emailByID'), "id",
                                  user_details.new_user_details.get('email'))

    def enter_phone(self):
        self.send_keys_to_element(map_driver_element.signup_page.get('phoneByID'), "id",
                                  user_details.new_user_details.get('phone'))

    def enter_company(self):
        self.send_keys_to_element(map_driver_element.signup_page.get('companyByID'), "id",
                                  user_details.new_user_details.get('company'))

    def select_number_of_employees(self):

        self.get_element(map_driver_element.signup_page.get('companyByID'), "id"). \
            send_keys(Keys.TAB, Keys.ENTER, Keys.ARROW_DOWN, Keys.ENTER)
        # self.sleep_time(25)
        # self.click_on_element(map_driver_element.signup_page.get('employeesByXpath'), "xpath")
        # self.sleep_time(3)
        # self.click_on_element(map_driver_element.signup_page.get('selectEmployeeByXpath'), "xpath")

    def agree_privacy(self):
        self.click_on_element(map_driver_element.signup_page.get('privacyByID'), "id")

    def click_free_trial(self):
        self.sleep_time(5)
        self.click_on_element(map_driver_element.signup_page.get('freeTrialButtonByXpath'), "xpath")
