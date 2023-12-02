from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    login_form = (By.CSS_SELECTOR, "#login_form")
    passw_form = (By.CSS_SELECTOR, "#register_form")
    EMAIL = (By.XPATH, "//*[@id='register_form']/div[1]/div/input")
#     PASS1 = (By.XPATH, "//*[@id='id_registration-password1']")
#     PASS2 = (By.XPATH, "//*[@id='id_registration-password2']")
    PASS1 = (By.CSS_SELECTOR, '#id_registration-password1')
    PASS2 = (By.CSS_SELECTOR, '#id_registration-password2')

    REGISTER_BUTTON = (By.XPATH, "//button[@name='registration_submit']")

class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.XPATH, "//button[contains(@class, 'btn-add-to-basket')]")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".row h1")
    ADD_TO_BASKET_MESSAGE = (By.XPATH, "//*[@id='messages']/div[1]/div/strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main p[class='price_color']")
    BASKET_PRICE = (By.CSS_SELECTOR, "div.alert div p strong")
    
class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_BUTTON = (By.CSS_SELECTOR, "span[class='btn-group'] a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators:
    MESSAGE_EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner")
    ITEMS_TO_BUY_NOW = (By.CSS_SELECTOR, ".basket-items")

    