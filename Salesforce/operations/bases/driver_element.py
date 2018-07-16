from selenium import webdriver
from bases.base_setup import BaseSetup
from selenium.webdriver.common.by import By
import time


class DriverElements:

    def __init__(self, driver):
        self.driver = driver

    def get_locator_type(self, locator_type):
        locator_type = locator_type.lower()

        if locator_type == "id":
            return By.ID
        elif locator_type == "xpath":
            return By.XPATH
        elif locator_type == "class_name":
            return By.CLASS_NAME
        elif locator_type == "css_selector":
            return By.CSS_SELECTOR
        elif locator_type == "link_text":
            return By.LINK_TEXT
        elif locator_type == "name":
            return By.NAME
        elif locator_type == "tag_name":
            return By.TAG_NAME
        else:
            raise Exception("Invalid Locator specified")

    def get_element(self, locator, locator_type=""):
       try:
            by_type = self.get_locator_type(locator_type)
            element = self.driver.find_element(by_type, locator)
            return element
       except Exception:
           raise Exception("Element {0} is not found".format(locator))

    def get_elements(self, locator, locator_type=""):
        try:
            by_type = self.get_locator_type(locator_type)
            elements = []
            elements.append(self.driver.find_elements(by_type, locator))
            return elements
        except Exception:
            raise Exception("Element {0} is not found".format(locator))

    def click_on_element(self, locator, locator_type=""):
        by_type = self.get_locator_type(locator_type)
        element = self.driver.find_element(by_type, locator)
        element.click()

    def send_keys_to_element(self, locator, locator_type="", data=""):
        by_type = self.get_locator_type(locator_type)
        element = self.driver.find_element(by_type, locator)
        element.send_keys(data)

    def element_is_visible(self, locator, locator_type=""):
        try:
            by_type = self.get_locator_type(locator_type)
            boolean = self.driver.find_element(by_type, locator).is_enabled()
            return boolean
        except Exception:
            raise Exception('Element {0} is not displayed'.format(locator))

    def element_is_visible_using_element(self, element):
        try:
            boolean = element.is_enabled()
            return boolean
        except Exception:
            raise Exception('Element {0} is not displayed'.format(element))

    def click_returned_element(self, element):
        element.click()

    def sleep_time(self, interval=2):
        time.sleep(interval)


