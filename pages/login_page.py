from .base_page import BasePage
from .locators import MainPageLocators
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
        current_url = self.browser.current_url
        assert "login" in str(current_url), "The login string is absent in url"
       

    def should_be_login_form(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "The login form is not found"

    def should_be_register_form(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "The register form is not found"
        