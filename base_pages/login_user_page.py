from selenium.webdriver.common.by import By


class login_user_page:

    # locator
    textbox_user_id = '//*[@id="Email"]'
    textbox_password = '//*[@id="Password"]'
    button_login = '//*[@id="main"]/div/div/div/div[2]/div[1]/div[2]/form/div[3]/button'

    # constructor
    def __init__(self, driver):
        self.driver = driver

    #action method
    def enter_user_id(self, username):
        self.driver.find_element(By.XPATH, self.textbox_user_id).clear()
        self.driver.find_element(By.XPATH, self.textbox_user_id).send_keys(username)
    def enter_password(self, password):
        self.driver.find_element(By.XPATH, self.textbox_password).clear()
        self.driver.find_element(By.XPATH, self.textbox_password).send_keys(password)
    def click_login_btn(self):
        self.driver.find_element(By.XPATH, self.button_login).click()
