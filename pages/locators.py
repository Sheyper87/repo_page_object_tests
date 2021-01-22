from selenium.webdriver.common.by import By


class MainPageLocators():
    pass
    
class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")

class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    MESSAGE_ADD_TO_BASKET = (By.CSS_SELECTOR, ".alert.alert-safe.alert-noicon.alert-success:nth-child(1)")
    THE_BOOK_TITLE = (By.CSS_SELECTOR, "div.col-sm-6.product_main>h1")
    THE_BOOK_COST = (By.CSS_SELECTOR, "div.col-sm-6.product_main>p")
    THE_BASKET_TOTAL = (By.CSS_SELECTOR, ".alert.alert-safe.alert-noicon.alert-info .alertinner>p")
    
class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

class BasketPageLocators():
    BASKET_LINK = (By.CSS_SELECTOR, "span.btn-group>a.btn.btn-default")
    EMPTY_MESSAGE = (By.CSS_SELECTOR, "div#content_inner>p")
    PRODUCT = (By.CSS_SELECTOR, ".basket-title.hidden-xs")
    
    
    
    
    
    
    