from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import allure


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

        self.USERNAME = (By.ID, "user-name")
        self.PASSWORD = (By.ID, "password")
        self.LOGIN_BUTTON = (By.ID, "login-button")

    @allure.step("Авторизоваться под standard_user {username} - {password}")
    def login(self, username: str, password: str) -> "LoginPage":
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
        self.wait = WebDriverWait(self.driver, 20)

        self.BACKPACK = (By.NAME, "add-to-cart-sauce-labs-backpack")
        self.BOLT_T_SHIRT = (By.NAME, "add-to-cart-sauce-labs-bolt-t-shirt")
        self.ONESIE = (By.NAME, "add-to-cart-sauce-labs-onesie")
        self.CART_CONTAINER = (By.CSS_SELECTOR, ".shopping_cart_container")

    @allure.step("Добавьте в корзину три товара {product_locator}")
    def add_to_cart(self, product_locator: tuple) -> None:
        button = self.driver.find_element(*product_locator)
        button.click()

    @allure.step("Перейти в корзину")
    def go_to_cart(self) -> None:
        cart_btn = self.driver.find_element(*self.CART_CONTAINER)
        cart_btn.click()


class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)
        self.CHECKOUT_BUTTON = (By.ID, "checkout")

    @allure.step("Перейдите к оформлению")
    def checkout(self) -> "CartPage":
        checkout_btn = self.wait.until(
            EC.element_to_be_clickable(self.CHECKOUT_BUTTON))
        checkout_btn.click()
        return self


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)
        self.FIRST_NAME = (By.ID, "first-name")
        self.LAST_NAME = (By.ID, "last-name")
        self.POSTAL_CODE = (By.ID, "postal-code")
        self.CONTINUE = (By.ID, "continue")
        self.TOTAL = (By.CLASS_NAME, "summary_total_label")

    @allure.step("Заполните форму {first_name} - {last_name} - {postal_code}")
    def fill_form(self, first_name: str, last_name: str, postal_code: str) -> None:
        first_name = self.driver.find_element(
            *self.FIRST_NAME).send_keys(first_name)
        last_name = self.driver.find_element(
            *self.LAST_NAME).send_keys(last_name)
        postal_code = self.driver.find_element(
            *self.POSTAL_CODE).send_keys(postal_code)
        self.driver.find_element(*self.CONTINUE).click()

    @allure.step("Прочитайте итоговую стоимость")
    def verify_total(self) -> str:
        total_element = self.wait.until(
            EC.visibility_of_element_located(self.TOTAL))
        return total_element.text
