from selenium.webdriver.common.by import By


def test_form_submission(driver):
    # Откройте страницу https://httpbin.qa-territory.online/forms/post.
    driver.get("https://httpbin.qa-territory.online/forms/post")

    # Найдите поле ввода с названием custname.
    name_field = driver.find_element(By.NAME, "custname")

    # Введите в него ваше имя.
    name_field.send_keys("Екатерина")

    # Найдите кнопку Submit и нажмите на нее.
    submit_button = driver.find_element(
        By.XPATH, "//button[text()='Submit order']"
    )
    submit_button.click()

    # Проверьте, что форма отправилась
    assert driver.current_url.endswith("/post")
