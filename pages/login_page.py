import time
from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.keys import Keys

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.url, "login is not presented in URL"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.login_form), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.passw_form), "Register form is not presented"


    def register_new_user(self):
        email = str(time.time()) + "@fakemail.org"
        self.browser.find_element(*LoginPageLocators.EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.PASS1).send_keys('Test12345')
        self.browser.find_element(*LoginPageLocators.PASS2).send_keys('Test12345')
        self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON).click()