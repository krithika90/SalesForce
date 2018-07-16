from bases.base_setup import BaseSetup
from pages.homePage import HomePage
from pages.loginPage import LoginPage
from pages.signUpPage import SignUpPage
from pages.gmailPage import GmailPage


class SignUpLoginFeature(BaseSetup):

    def setup(self):
        self.basesetup = BaseSetup()
        driver = self.basesetup.setup()
        self.homepage = HomePage(driver)
        self.loginpage = LoginPage(driver)
        self.signuppage = SignUpPage(driver)
        self.gmailpage = GmailPage(driver)

    def verify_if_login_page_is_displayed(self):
        if self.loginpage.salesforce_logo():
            print('1-SalesForce Login page is displayed..')
        else:
            print('1-SalesForce Login Page is not displayed')

    def verify_signup_functionality(self):
        self.loginpage.signup_link()
        print('2-Navigated to SignUp Page')
        self.signuppage.enter_firstName()
        print('3-Entered First Name')
        self.signuppage.enter_lastName()
        print('4-Entered Last Name')
        self.signuppage.enter_jobTitle()
        print('5-Entered Job Title')
        self.signuppage.enter_email()
        print('6-Entered Email')
        self.signuppage.enter_phone()
        print('7-Entered Phone number')
        self.signuppage.enter_company()
        print('8-Entered Company name')
        self.signuppage.select_number_of_employees()
        print('9-Chose the number of employees')
        # self.signuppage.select_state()
        # print('10-Chose the state')
        self.signuppage.agree_privacy()
        print('11-Checked the Privacy Policy')
        self.signuppage.click_free_trial()
        print('12-Created user has auto logged in')

    def verify_signedup_user_is_logged_in(self):
        if self.homepage.verify_header():
            print('13-Header is displayed')
        if self.homepage.verify_page_title():
            print('14-User is logged in and Home Page with Dashboard is viewed')

    def verify_login_functionality(self):
        self.loginpage.username_login()
        self.loginpage.password_login()
        self.loginpage.login()

    def enter_verification_code(self, code):
        self.loginpage.verification_code(code)

    def tear_down(self):
        self.basesetup.tear_down()
