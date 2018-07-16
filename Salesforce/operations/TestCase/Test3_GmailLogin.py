from tests.gmailLogin_VerificationCode import GmailLoginVerificationCode

gmail = GmailLoginVerificationCode()
gmail.setup_gmail()
gmail.verify_Gmail_login_functionality()
gmail.verify_if_gmail_is_logged_in()
gmail.obtain_verification_code()
gmail.tear_down()
