from selenium.webdriver.common.by import By


def test_multiple_elements(driver):
    # Откройте страницу https://httpbin.qa-territory.online/links/10.
    driver.get("https://httpbin.qa-territory.online/links/10")

    # Найдите все ссылки на странице (тег <a>)
    links = driver.find_elements(By.TAG_NAME, "a")

    # Проверьте, что количество ссылок равно 9
    assert len(links) == 9
