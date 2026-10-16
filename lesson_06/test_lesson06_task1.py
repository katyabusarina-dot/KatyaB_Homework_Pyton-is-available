from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_dynamic_loading(driver):
    # 1. Откройте страницу https://the-internet.herokuapp.com/dynamic_loading/2
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")

    # 2. Найдите и нажмите на кнопку "Start"
    button = driver.find_element(By.CSS_SELECTOR, "#start button")
    button.click()

    # 3. Дождитесь появления текста "Hello World!"
    WebDriverWait(driver, 15).until(EC.text_to_be_present_in_element(
        (By.CSS_SELECTOR, "#finish"), "Hello World!"))

    # 4. Сделайте скриншот страницы
    driver.save_screenshot("screenshots/text_screen.png")

    # 5. Проверьте, что появившийся текст равен "Hello World!"
    hello_element = driver.find_element(By.CSS_SELECTOR, "#finish")
    assert hello_element.text == "Hello World!"
