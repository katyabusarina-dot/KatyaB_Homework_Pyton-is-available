from selenium import webdriver
from selenium.webdriver.common.by import By


def test_form_submission():
    driver = webdriver.Chrome()

# Откройте страницу https://httpbin.qa-territory.online/forms/post.
    driver.get("https://httpbin.qa-territory.online/forms/post")

# Найдите поле ввода с названием custname.
    name_field = driver.find_element(By.NAME, "custname")

# Введите в него ваше имя.
    name_field.send_keys("Екатерина")

# Найдите кнопку Submit и нажмите на нее.
    submit_button = driver.find_element(By.CLASS_NAME, "Submit")
    submit_button.click()

# Проверьте, что после нажатия URL изменился.
    assert driver.current_url == "https://httpbin.qa-territory.online/"

    driver.quit()
