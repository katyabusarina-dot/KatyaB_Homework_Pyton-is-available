import os
import pytest
import requests


base_url = "https://ru.yougile.com/api-v2"


@pytest.fixture(scope="session")
def api_key():
    """API-ключ из переменной окружения — не храним секреты в коде."""
    key = os.environ.get("API_KEY")
    assert key, "Задайте переменную окружения YOUGILE_API_KEY"
    return key


@pytest.fixture(scope="session")
def api_client(api_key):
    session = requests.Session()
    session.headers.update({
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    })
    return session


user_id = "b60fe264-8a08-43ae-ba8a-52f10cb4351e"
payload = {
    "title": "Создание ДЗ",
    "users": {
        user_id: {"role": "admin"},
    },
}


@pytest.fixture()
def pro_id(api_client):
    resp = requests.post(f"{base_url}/projects", api_client, json=payload)
    assert resp.status_code == 201
    project_id = resp.json()["id"]
    yield project_id
    requests.delete(f"{base_url}/projects/{project_id}")
