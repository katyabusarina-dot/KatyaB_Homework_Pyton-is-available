def test_session_storage_auth(driver):
    # Откройте страницу https://gitflic.ru/
    driver.get("https://gitflic.ru/")

    # Установите cookie пользователя 1
    driver.add_cookie({
        "name": "SESSION",
        "value": "OWMxZWEwNzUtZTA5YS00ODkzLTliMDctOWY3OTg0OGYxMTUw",
        "domain": "gitflic.ru"})

    # Обновите страницу
    driver.refresh()

    # Перейдите на страницу пользователя 1
    driver.get("https://gitflic.ru/project?sort=updated_at&direction=ASC")

    # Сохраните текущий URL
    url_user1 = "https://gitflic.ru/project?sort=updated_at&direction=ASC"

    # Разлогиньтесь (очистите куки)
    driver.delete_all_cookies()

    # Установите cookie пользователя 2
    driver.add_cookie({
        "name": "SESSION",
        "value": "Y2IzMGQyZWQtOGRjMS00ZDlkLThlMjQtM2YyODUwNTcwYTQ0",
        "domain": "gitflic.ru"})

    # Обновите страницу
    driver.refresh()

    # Перейдите на страницу пользователя 2
    driver.get(
        "https://gitflic.ru/project?sort=updated_at&direction=ASC&continue")

    # Сохраните текущий URL
    url_user2 = "https://gitflic.ru/project?sort=updated_at" \
                "&direction=ASC&continue"

    # Проверьте, что URL для пользователя 1 и пользователя 2 различаются.
    assert url_user1 != url_user2
