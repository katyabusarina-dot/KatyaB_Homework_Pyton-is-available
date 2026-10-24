import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    yield driver

def test_shop(driver):
    options = webdriver.FirefoxOptions()
    driver = webdriver.Firefox(options=options)
    wait = WebDriverWait(driver, 10)
    
# Откройте сайт магазина: https://www.saucedemo.com/ в FireFox.
    driver.get("https://www.saucedemo.com/")

# Авторизуйтесь как пользователь standard_user
    wait.until(EC.visibility_of_element_located(
        (By.ID, "user-name"))).send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

# Добавьте в корзину товары( Sauce Labs Backpack,
# Sauce Labs Bolt T-Shirt, Sauce Labs Onesie)
    driver.find_element(By.NAME, "add-to-cart-sauce-labs-backpack").click()
    driver.find_element(By.NAME, "add-to-cart-sauce-labs-bolt-t-shirt").click()
    driver.find_element(By.NAME, "add-to-cart-sauce-labs-onesie").click()

# Перейдите в корзину
    wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, ".shopping_cart_container"))).click()

# Нажмите Checkout.
    wait.until(EC.element_to_be_clickable((By.ID, "checkout"))).click()

# Заполните форму своими данными(имя,фамилия,почтовый индекс)
    wait.until(EC.visibility_of_element_located((
        By.ID, "first-name"))).send_keys("Екатерина")
    driver.find_element(By.ID, "last-name").send_keys("Бусарина")
    driver.find_element(By.ID, "postal-code").send_keys("864792")

# Нажмите кнопку Continue.
    driver.find_element(By.ID, "continue").click()

# Прочитайте со страницы итоговую стоимость ( Total).
    total_text = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label"))
        )
    total_text = wait.until(EC.visibility_of_element_located(
        (By.CLASS_NAME, "summary_total_label")))
    driver.execute_script("arguments[0].scrollIntoView();", total_text),
    print(f"Получена итоговая стоимость: {total_text}")

# Проверьте, что итоговая сумма равна $58.29
    assert total_text.text == 'Total: $58.29'
    
    driver.quit()
