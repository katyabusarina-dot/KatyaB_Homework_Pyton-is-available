from selenium import webdriver
from selenium.webdriver.common.by import By


def test_navigation():
    driver = webdriver.Chrome()

# Откройте страницу https://httpbin.qa-territory.online
    driver.get("https://httpbin.qa-territory.online")

# Найдите и кликните на ссылку HTML Form
    driver.find_element(By.LINK_TEXT, "HTML Forms").click()

# Проверьте, что URL изменился на /forms/post
    assert driver.current_url.endswith("/forms/post")

# Вернитесь назад на главную страницу
    driver.back()

# Проверьте, что вернулись на исходный URL
    assert driver.current_url == "https://httpbin.qa-territory.online"
    driver.quit()
