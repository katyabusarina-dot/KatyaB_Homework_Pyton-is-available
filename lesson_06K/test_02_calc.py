import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_calc(driver):
# Откройте страницу
    wait = WebDriverWait(driver, 60)
    driver.get("https://bonigarcia.dev/selenium" \
        "-webdriver-java/slow-calculator.html")

# В поле ввода по локатору #delay введите значение 45
    delay_input = driver.find_element(By.CSS_SELECTOR, "#delay")
    delay_input.clear()
    delay_input.send_keys("45")

# Нажмите на кнопки: 7, +, 8, =
    driver.find_element(By.XPATH, "//span[text()='7']").click()
    driver.find_element(By.XPATH, "//span[text()='+']").click()
    driver.find_element(By.XPATH, "//span[text()='8']").click()
    driver.find_element(By.XPATH, "//span[text()='=']").click()

# Проверьте (assert), что в окне отобразится результат 15 через 45 секунд
    result_is_correct = wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15"))

    assert result_is_correct
    print("Тест пройден: результат равен 15.")
    driver.save_screenshot("screenshots/screen.png")

    
