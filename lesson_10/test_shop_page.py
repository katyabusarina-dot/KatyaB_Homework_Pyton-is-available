from selenium import webdriver
from pages.shop_page import LoginPage, MainPage, CartPage, CheckoutPage
import allure


@allure.title("Интернет_магазин")
@allure.feature("Оформление заказа")
@allure.description("Итоговая стоимость корзины из трёх товаров равна $58.29")
@allure.severity("CRITIСAL")
def test_shop():
    options = webdriver.FirefoxOptions()
    driver = webdriver.Firefox(options=options)
    try:

        with allure.step("Открыть сайт магазина"):
            driver.get("https://www.saucedemo.com/")

        with allure.step("Авторизоваться под standard_user"):
            login_page = LoginPage(driver)
            login_page.login("standard_user", "secret_sauce")

        with allure.step("Добавьте в корзину три товара и " \
        "перейдите в корзину"):
            main_page = MainPage(driver)
            main_page.add_to_cart(main_page.BACKPACK)
            main_page.add_to_cart(main_page.BOLT_T_SHIRT)
            main_page.add_to_cart(main_page.ONESIE)
            main_page.go_to_cart()

        with allure.step("Перейдите к оформлению"):
            cart_page = CartPage(driver)
            cart_page.checkout()

        with allure.step("Заполните форму и прочитайте итоговую стоимость"):
            checkout_page = CheckoutPage(driver)
            checkout_page.fill_form("Екатерина", "Бусарина", "864792")

        total_text = checkout_page.verify_total()
        print(f"Получена итоговая стоимость: {total_text}")

        with allure.step("Проверьте, что итоговая сумма равна $58.29"):
            assert total_text == "Total: $58.29", \
                f"Ожидалась сумма 'Total: $58.29', получено: '{total_text}'"
    finally:
        driver.quit()
