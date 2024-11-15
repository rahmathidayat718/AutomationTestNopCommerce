from selenium.webdriver.common.by import By
from selenium.webdriver.edge import webdriver
from selenium import webdriver
from base_pages.login_user_page import login_user_page
import pytest


class Test_01_user_login:
    user_page_url = "https://demo.nopcommerce.com/login"
    user_id = "rohmatmingil@gmail.com"
    password = "user_login123"
    invalid_username = "yey@mail.com"
    invalid_password = "yes"

    #Verify user_login_page
    def test_title_verification(self):
        self.driver = webdriver.Edge()
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
    def test_valid_user_login(self):
        self.driver = webdriver.Edge()
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

    def test_invalid_user_login(self):
        self.driver = webdriver.Edge()
        self.driver.get(self.user_page_url)
        self.user_lp = login_user_page(self.driver)
        self.user_lp.enter_user_id(self.invalid_username)
        self.user_lp.enter_password(self.password)
        self.user_lp.click_login_btn()
        error_message = self.driver.find_element(By.XPATH, '//*[@id="main"]/div/div/div/div[2]/div[1]/div[2]/form/div[1]/ul/li').text
        if error_message == "No customer account found":
            assert True
            self.driver.close()
        else:
            self.driver.close()
            assert False

