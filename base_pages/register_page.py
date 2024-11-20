

class register_page:
    # Locator
    first_name_id = "FirstName"
    last_name_id = "LastName"
    gender = ""
    date_of_birth = ""
    email_id= "Email"
    company_name_id = "Company"
    password_id = "Password"
    confirm_password_id = "ConfirmPassword"
    btn_register_xpath = '//*[@id="register-button"]'

    # constructor
    def __init__(self, driver):
        self.driver = driver

    # Action method

