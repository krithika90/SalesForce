login_page = dict(
    logoByXpath='//img[@src="/img/logo214.svg"]',
    usernameByID="username",
    passwordByID="password",
    loginButtonById="Login",
    tryForFreelinkByID="signup_link",
    verificationCodeByXpath='//*[@class="formArea"]/input',
    verifyButtonByXpath='//input[@value="Verify"]'
)

signup_page = dict(
    firstNameByID="UserFirstName",
    lastNameByID="UserLastName",
    jobTitleByXpath='//div[@class="control-container"]/div[2]/select[1]/option[1][text()="Job title"]',
    jobTitleChooseByXpath='//div[@class="control-container"]/div[2]/select[1]/option[5][text()="Sales_Manager_AP"]',
    emailByID='UserEmail',
    phoneByID="UserPhone",
    companyByID="CompanyName",
    employeesByXpath='//*[@id="CompanyEmployees"]/option[1]',
    selectEmployeeByXpath='//*[@id="CompanyEmployees"]/option[2]',
    stateByID="CompanyState",
    chooseStateByXpath='',
    privacyByID="SubscriptionAgreement",
    freeTrialButtonByXpath='//*[@id="form-container"]/div[2]/div/a/span'
)

home_page = dict(
    headerByXpath='//*[@id="oneHeader"]/div[2]',
    pageTitleByXpath='//html/head/title'
)

gmail_page = dict(
    usernameByID='identifierId',
    nextByXpath='//*[text()="Next"]',
    passwordByName='password',
    recoveryOptionByXpath='//*[text()="Confirm your recovery phone number"]',
    recoveryEnterPhoneNoByID='phoneNumberId',
    navigateToGmailByXpath='//a[@href="https://mail.google.com"]',
    inboxByXpath='//*[text()="COMPOSE"]',
    verificationMailItemByXpath='//span[@class="y2"]',
    verificationCodeByXpath='//div[@class="HOEnZb"]'
)
