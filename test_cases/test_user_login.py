import time
from selenium.webdriver.common.by import By
from base_pages.login_user_page import login_user_page
from utilities.read_properties import Read_config


class Test_01_user_login:
    user_page_url = Read_config.get_url_login()
    user_id = Read_config.get_user_id()
    password = Read_config.get_password()
    invalid_user_id = Read_config.get_invalid_user_id()
    invalid_password = Read_config.get_invalid_password()

    #Verify user_login_page
    def test_title_verification(self, setup):
        self.driver = setup
        self.driver.get(self.user_page_url)

        act_title = self.driver.find_element(By.XPATH, '//*[@id="main"]/div/div/div/div[1]/h1').text
        exp_title = "Welcome, Please Sign In!"
        if act_title == exp_title:
            assert True
            self.driver.close()
        else:
            self.driver.close()
            assert False

    #tase case
    def test_valid_user_login(self, setup):
        self.driver = setup
        self.driver.get(self.user_page_url)
        self.user_lp = login_user_page(self.driver)
        self.user_lp.enter_user_id(self.user_id)
        self.user_lp.enter_password(self.password)
        self.user_lp.click_login_btn()
        act_welcome_text = self.driver.find_element(By.XPATH, '//*[@id="main"]/div/div/div/div/div[2]/div[1]/h2').text
        if act_welcome_text == "Welcome to our store":
            assert True
            self.driver.close()
        else:
            self.driver.close()
            assert False

    def test_invalid_user_login(self, setup):
        self.driver = setup
        self.driver.get(self.user_page_url)
        self.user_lp = login_user_page(self.driver)
        self.user_lp.enter_user_id(self.invalid_user_id)
        self.user_lp.enter_password(self.password)
        self.user_lp.click_login_btn()
        error_message = self.driver.find_element(By.XPATH, '//*[@id="main"]/div/div/div/div[2]/div[1]/div[2]/form/div[1]/ul/li').text
        if error_message == "No customer account found":
            assert True
            self.driver.close()
        else:
            self.driver.close()
            assert False

