from bases.base_setup import BaseSetup
from pages.gmailPage import GmailPage

class GmailLoginVerificationCode(BaseSetup):

    def setup_gmail(self):
        self.basesetup = BaseSetup()
        driver = self.basesetup.setup_gmail()
        self.gmailpage = GmailPage(driver)

    def verify_Gmail_login_functionality(self):
        self.gmailpage.enter_gmail_username()
        print('Entered GMail Username')
        self.gmailpage.click_next_button()
        self.gmailpage.enter_password()
        print('Entered GMail Password')
        self.gmailpage.click_next_button()
        #self.gmailpage.enter_phone_no_for_recovery()
        #self.gmailpage.click_next_button()
        self.gmailpage.navigate_to_gmail()

    def verify_if_gmail_is_logged_in(self):
        if self.gmailpage.inbox_link():
            print('User is logged into GMail')
        else:
            print('GMail Login Failed')

    def obtain_verification_code(self):
        self.gmailpage.salesforce_mail_item()
        print('Opened the mail item')
        verification_code = self.gmailpage.get_verification_code()
        return verification_code

    def tear_down(self):
        self.basesetup.tear_down()
