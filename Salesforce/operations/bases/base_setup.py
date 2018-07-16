from bases.browser_setup import browser_setup
from selenium import webdriver
import datetime


class BaseSetup(object):

    def setup(self):
        print('Setting up environment +'+str(datetime.datetime.now()))
        if browser_setup["browser"] == "chrome":
            self.driver = webdriver.Chrome()
        elif browser_setup["browser"] == "firefox":
            self.driver = webdriver.Firefox()
        else:
            raise Exception("Mentioned browser is not supported")

        self.driver.maximize_window()
        self.driver.delete_all_cookies()
        self.driver.get(browser_setup["url"])
        return self.driver

    def setup_gmail(self):
        if browser_setup["browser"] == "chrome":
            self.driver = webdriver.Chrome()
        elif browser_setup["browser"] == "firefox":
            self.driver = webdriver.Firefox()
            self.driver.url
        else:
            raise Exception("Mentioned browser is not supported")

        self.driver.maximize_window()
        self.driver.delete_all_cookies()
        self.driver.get(browser_setup["gmail_url"])
        return self.driver

    def tear_down(self):
        print('Tearing down environment +'+str(datetime.datetime.now()))
        self.driver.quit()
