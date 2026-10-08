from selenium.webdriver.common.by import By


def test_navigation(driver):
    # Откройте страницу https://httpbin.qa-territory.online
    driver.get("https://httpbin.qa-territory.online")

    # Найдите и кликните на ссылку HTML Form
    driver.find_element(By.LINK_TEXT, "HTML Form").click()

    # Проверьте, что перешли на страницу формы
    assert driver.current_url.endswith("/forms/post")
