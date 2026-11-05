from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

        self.USERNAME = (By.ID, "user-name")
        self.PASSWORD = (By.ID, "password")
        self.LOGIN_BUTTON = (By.ID, "login-button")

    def login(self, username, password):
        username_field = self.wait.until(
            EC.visibility_of_element_located(self.USERNAME))
        username_field.clear()
        username_field.send_keys(username)

        password_field = self.driver.find_element(*self.PASSWORD)
        password_field.clear()
        password_field.send_keys(password)

        login_button = self.driver.find_element(*self.LOGIN_BUTTON)
        login_button.click()
        return self


class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.BACKPACK = (By.NAME, "add-to-cart-sauce-labs-backpack")
        self.BOLT_T_SHIRT = (By.NAME, "add-to-cart-sauce-labs-bolt-t-shirt")
        self.ONESIE = (By.NAME, "add-to-cart-sauce-labs-onesie")
        self.CART_CONTAINER = (By.CSS_SELECTOR, ".shopping_cart_container")

    def add_to_cart(self, product_name):
        product_name = self.driver.find_element(
            By.XPATH, f"//button[text()='Add to cart' and @data-test='{
                product_name}']").click()

    def go_to_cart(self):
        self.driver.find_element(self.CART_CONTAINER).click()


class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.CHECKOUT_BUTTON = (By.ID, "checkout")

    def checkout(self):
        checkout_btn = self.wait.until(
            EC.element_to_be_clickable(self.CHECKOUT_BUTTON))
        checkout_btn.click()
        return self


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.FIRST_NAME = (By.ID, "first-name")
        self.LAST_NAME = (By.ID, "last-name")
        self.POSTAL_CODE = (By.ID, "postal-code")
        self.CONTINUE = (By.ID, "continue")
        self.TOTAL = (By.CLASS_NAME, "summary_total_label")

    def fill_form(self, first_name, last_name, postal_code):
        first_name = self.driver.find_element(
            self.FIRST_NAME).send_keys(first_name)
        last_name = self.driver.find_element(
            self.LAST_NAME).send_keys(last_name)
        postal_code = self.driver.find_element(
            self.POSTAL_CODE).send_keys(postal_code)
        self.driver.find_element(self.CONTINUE).click()

    def verify_total(self):
        total_element = self.wait.until(
            EC.visibility_of_element_located(self.TOTAL))
        return total_element.text
