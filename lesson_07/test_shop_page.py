from selenium import webdriver
from pages.shop_page import LoginPage, MainPage, CartPage, CheckoutPage


def test_shop():
    options = webdriver.FirefoxOptions()
    driver = webdriver.Firefox(options=options)
    try:

        # Откройте сайт магазина в Firefox
        driver.get("https://www.saucedemo.com/")

        # Авторизуйтесь как standard_user
        login_page = LoginPage(driver)
        login_page.login("standard_user", "secret_sauce")

        # Добавьте в корзину три товара и перейдите в корзину
        main_page = MainPage(driver)
        main_page.add_to_cart(main_page.BACKPACK)
        main_page.add_to_cart(main_page.BOLT_T_SHIRT)
        main_page.add_to_cart(main_page.ONESIE)
        main_page.go_to_cart()

        # Перейдите к оформлению
        cart_page = CartPage(driver)
        cart_page.checkout()

        # Заполните форму и прочитайте итоговую стоимость
        checkout_page = CheckoutPage(driver)
        checkout_page.fill_form("Екатерина", "Бусарина", "864792")

        total_text = checkout_page.verify_total()
        print(f"Получена итоговая стоимость: {total_text}")

        # Проверьте, что итоговая сумма равна $58.29
        assert total_text == "Total: $58.29", \
            f"Ожидалась сумма 'Total: $58.29', получено: '{total_text}'"
    finally:
        driver.quit()
