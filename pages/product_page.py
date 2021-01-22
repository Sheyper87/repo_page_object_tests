from .base_page import BasePage
from .locators import ProductPageLocators
from .locators import BasketPageLocators



class ProductPage(BasePage):

    
    def add_to_basket(self):
        basket_link = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        basket_link.click()

    
    def book_title_should_match_the_message(self):
        book_title = self.browser.find_element(*ProductPageLocators.THE_BOOK_TITLE)
        message_add_to_basket = self.browser.find_element(*ProductPageLocators.MESSAGE_ADD_TO_BASKET)
        assert book_title.text + " " + "book"  != ' '.join(message_add_to_basket.text.split() [1:5]), "The book title is absent in adding to basket message"
        
    def book_cost_should_match_the_basket_total(self):    
        book_cost = self.browser.find_element(*ProductPageLocators.THE_BOOK_COST)
        basket_total = self.browser.find_element(*ProductPageLocators.THE_BASKET_TOTAL)
        assert book_cost.text.split(" £") [0] == basket_total.text.split(" ") [4], "The book cost is not equal to basket total cost"
    
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE_ADD_TO_BASKET), "Success message is presented, but should not be"
        
    def should_not_be_success_message2(self):
        assert self.is_disappeared(*ProductPageLocators.MESSAGE_ADD_TO_BASKET), "Success message should disappear but it does not dissapear"
        