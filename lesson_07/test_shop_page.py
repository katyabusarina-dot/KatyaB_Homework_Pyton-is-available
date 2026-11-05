from selenium import webdriver
from pages.shop_page import LoginPage, MainPage, CartPage, CheckoutPage


def test_shop():
    options = webdriver.FirefoxOptions()
    driver = webdriver.Firefox(options=options)

# Откройте сайт магазина: https://www.saucedemo.com/ в FireFox.
    driver.get("https://www.saucedemo.com/")

# Авторизуйтесь как пользователь standard_user
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")

# Добавьте в корзину товары( Sauce Labs Backpack,
# Sauce Labs Bolt T-Shirt, Sauce Labs Onesie)
    main_page = MainPage(driver)
    main_page.add_backpack() \
             .add_tshirt() \
             .add_onesie() \
             .go_to_cart()

# Перейдите в корзину
    cart_page = CartPage(driver)
    cart_page.click_checkout()

# Заполните форму своими данными(имя,фамилия,почтовый индекс)
    checkout_page = CheckoutPage(driver)
    checkout_page.fill_form("Екатерина", "Бусарина", "864792")

# Прочитайте со страницы итоговую стоимость ( Total).
    total_text = checkout_page.get_total_price()
    print(f"Получена итоговая стоимость: {total_text}")

# Проверьте, что итоговая сумма равна $58.29
    assert total_text.text == 'Total: $58.29'

    driver.quit()
