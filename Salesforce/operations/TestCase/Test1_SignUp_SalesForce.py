from tests.signupandlogin import SignUpLoginFeature

sign = SignUpLoginFeature()
sign.setup()
sign.verify_if_login_page_is_displayed()
sign.verify_signup_functionality()
sign.verify_signedup_user_is_logged_in()
sign.tear_down()