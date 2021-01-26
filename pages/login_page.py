from .base_page import BasePage
from .locators import MainPageLocators
from .locators import LoginPageLocators
from .locators import BasePageLocators
from .locators import RegisterPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()
        current_url = self.browser.current_url
        assert "login" in str(current_url), "The login string is absent in url"
       

    def should_be_login_form(self):
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "The login form is not found"

    def should_be_register_form(self):
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "The register form is not found"
    
    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*RegisterPageLocators.EMAIL_FIELD)
        email_field.send_keys(email)
        password_field = self.browser.find_element(*RegisterPageLocators.PASSWORD_FIELD)
        password_field.send_keys(password)
        confirm_password = self.browser.find_element(*RegisterPageLocators.CONFIRM_PASS)
        confirm_password.send_keys(password)
        register_button = self.browser.find_element(*RegisterPageLocators.REGISTER_BUTTON)
        register_button.click()
        
        