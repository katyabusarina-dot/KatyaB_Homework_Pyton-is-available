from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_form():
    # Для локального запуска можно заменить на webdriver.Chrome()
    driver = webdriver.Edge() 
    wait = WebDriverWait(driver, 10)
    
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    # Заполняем форму
    driver.find_element(By.NAME, "first-name").send_keys("Иван")
    driver.find_element(By.NAME, "last-name").send_keys("Петров")
    driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
    driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
    driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
    driver.find_element(By.NAME, "city").send_keys("Москва")
    driver.find_element(By.NAME, "country").send_keys("Россия")
    driver.find_element(By.NAME, "job-position").send_keys("QA")
    driver.find_element(By.NAME, "company").send_keys("SkyPro")

    # Нажимаем Submit
    button = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "button[type='submit']")))
    driver.execute_script("arguments[0].scrollIntoView();", button)
    button.click()

    # ЖДЕМ, пока страница перестроится и поле появится
    zip_code_element = wait.until(EC.presence_of_element_located((By.ID, 'zip-code')))
    border_color = zip_code_element.value_of_css_property('border-color')
    assert border_color == 'rgb(245, 194, 199)', f"Цвет Zip code: {border_color}"

    # Ждем и проверяем остальные поля
    valid_fields_ids = [
        "first-name", "last-name", "address", "e-mail",
        "phone", "city", "country", "job-position", "company"
    ]

    for field_id in valid_fields_ids:
        element = wait.until(EC.presence_of_element_located((By.ID, field_id)))
        border_color = element.value_of_css_property('border-color')
        assert border_color == 'rgb(186, 219, 204)', f"Поле {field_id} не зеленое! Цвет: {border_color}"

    driver.quit()
