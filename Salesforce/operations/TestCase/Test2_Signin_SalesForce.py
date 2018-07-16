from tests.signupandlogin import SignUpLoginFeature
from tests.gmailLogin_VerificationCode import GmailLoginVerificationCode

sign = SignUpLoginFeature()
gmail = GmailLoginVerificationCode()

sign.setup()
sign.verify_if_login_page_is_displayed()
sign.verify_login_functionality()

gmail.setup_gmail()
gmail.verify_Gmail_login_functionality()
gmail.verify_if_gmail_is_logged_in()
code = gmail.obtain_verification_code()
sign.enter_verification_code(code)
gmail.tear_down()

sign.verify_signedup_user_is_logged_in()

sign.tear_down()
