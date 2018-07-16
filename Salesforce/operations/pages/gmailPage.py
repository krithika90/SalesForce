from bases.base_setup import BaseSetup
from bases.driver_element import DriverElements
from tests import map_driver_element
from tests import user_details
import re


class GmailPage(BaseSetup, DriverElements):

    def __init__(self, driver):
        driveele = DriverElements(driver)
        self.driver = driver

    def enter_gmail_username(self):
        self.sleep_time(10)
        self.send_keys_to_element(map_driver_element.gmail_page.get
                                  ('usernameByID'), "id", user_details.gmail_user_details.get('username'))

    def click_next_button(self):
        self.click_on_element(map_driver_element.gmail_page.get('nextByXpath'), "xpath")

    def enter_password(self):
        self.sleep_time(3)
        self.send_keys_to_element(map_driver_element.gmail_page.get('passwordByName'), "name",
                                  user_details.gmail_user_details.get('password'))

    # def enter_phone_no_for_recovery(self):
        #self.sleep_time(8)
        #if self.element_is_visible(self.get_element(map_driver_element.gmail_page.
        #                                                 get('recoveryOptionByXpath'), "xpath")):
        #     element = self.get_element(map_driver_element.gmail_page.get('recoveryOptionByXpath'), "xpath")
        #     self.click_returned_element(element)
        #     self.sleep_time()
        #     self.send_keys_to_element(map_driver_element.gmail_page.get('recoveryEnterPhoneNoByID'), "ID",
        #                               user_details.gmail_user_details.get('recoveryPhoneNo'))
        # else:
        #     pass

    def navigate_to_gmail(self):
        self.sleep_time(5)
        self.click_on_element(map_driver_element.gmail_page.get('navigateToGmailByXpath'), "xpath")

    def inbox_link(self):
        boolean = ""
        self.sleep_time(15)
        if self.element_is_visible(map_driver_element.gmail_page.get('inboxByXpath'), "xpath"):
            boolean = True
        return boolean

    def salesforce_mail_item(self):
        # self.sleep_time(20)
        element = self.get_element(map_driver_element.gmail_page.get('verificationMailItemByXpath'), "xpath")
        if self.element_is_visible_using_element(element):
            self.click_returned_element(element)

    def get_verification_code(self):
        self.sleep_time(3)
        self.click_on_element(map_driver_element.gmail_page.get('trimmedContentByXpath'), "xpath")
        self.sleep_time()
        mailbody = self.get_element(map_driver_element.gmail_page.
                                    get('verificationCodeByXpath'), "xpath").text
        numbers = ''
        for body in mailbody:
            if re.search(r'[0-9]', body):
                numbers = numbers+body

        verification_code = numbers[-5:]
        print('Obtained verification code {0}'.format(verification_code))
        return verification_code

