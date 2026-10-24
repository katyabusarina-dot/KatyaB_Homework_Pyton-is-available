import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    yield driver
    driver.quit()


def test_form(driver):
    driver = webdriver.Edge()

# Открыть страницу https://bonigarcia.dev/selenium-"
#     "webdriver-java/data-types.html в браузер
    wait = WebDriverWait(driver, 60)
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
    )

# Заполните форму значениями:
    wait.until(EC.visibility_of_element_located(
         (By.NAME, "first-name"))).send_keys("Иван")
    driver.find_element(By.NAME, "last-name").send_keys("Петров")
    driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
    driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
    driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
    driver.find_element(By.NAME, "city").send_keys("Москва")
    driver.find_element(By.NAME, "country").send_keys("Россия")
    driver.find_element(By.NAME, "job-position").send_keys("QA")
    driver.find_element(By.NAME, "company").send_keys("SkyPro")

# Нажмите кнопку Submit
    button = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "button[type='submit']")))
    driver.execute_script("arguments[0].scrollIntoView();", button)
    button.click()

# Проверьте (assert), что поле Zip code подсвечено красным
    zip_code_element = driver.find_element(By.ID, 'zip-code')
    border_color = zip_code_element.value_of_css_property('border-color')
    assert border_color == 'rgb(245, 194, 199)'
    driver.save_screenshot("screenshots/color_red.png")

# Проверьте (assert), что остальные поля подсвечены зеленым
    valid_fields_locators = [
        (By.NAME, "first-name"),
        (By.NAME, "last-name"),
        (By.NAME, "address"),
        (By.NAME, "e-mail"),
        (By.NAME, "phone"),
        (By.NAME, "city"),
        (By.NAME, "country"),
        (By.NAME, "job-position"),
        (By.NAME, "company")
    ]
    wait.until(EC.presence_of_all_elements_located(valid_fields_locators))

    for locator in valid_fields_locators:
        wait.until(EC.presence_of_element_located(locator))
        print(f"Элемент с локатором {locator} найден.")
        elements = driver.find_elements(*locator)

    border_color = elements.value_of_css_property('border-color')

    assert border_color == 'rgb(186, 219, 204)'
    driver.save_screenshot("screenshots/color_green.png")
