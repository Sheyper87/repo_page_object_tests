from .locators import BasketPageLocators
from .locators import ProductPageLocators
from .base_page import BasePage

class BasketPage(BasePage):
    def should_not_be_product(self):
        
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT), "The product should not be in a basket!"
        
    def should_be_empty_message(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_MESSAGE), "Empty message must appear"