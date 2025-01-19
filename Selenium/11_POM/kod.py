from selenium import webdriver
from selenium.webdriver.common.by import By

# Page Object Model

class LoginPage:
    def __init__(self, driver):
        self.driver = driver


    def open(self):
        self.driver.get('http://www.saucedemo.com')
        self.username_field_id = 'user-name'
        self.password_field_id = 'password'
        self.login_button_name = 'login-button'

    def print_page_info(self):
        print('Nazwa strony', self.driver.title)
        print('adres', self.driver.current_url)

    def enter_username(self, username):
        field = self.driver.find_element(By.ID, self.username_field_id)
        field.send_keys(username)

    def enter_password(self):
        pass
    def click_login(self):
        pass


    def close(self):
        self.driver.quit()

