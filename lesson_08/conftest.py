import os
import pytest
import requests
from dotenv import load_dotenv

load_dotenv()

base_url = "https://ru.yougile.com/api-v2"


@pytest.fixture(scope="session")
def api_key():
    key = os.environ.get("API_KEY")
    assert key, "Задайте переменную окружения API_KEY"
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
    "user_id": "admin"}


@pytest.fixture
def pro_id(api_client):
    resp = api_client.post(f"{base_url}/projects", json=payload)
    assert resp.status_code == 201, resp.text
    project_id = resp.json()["id"]
    yield project_id
    api_client.put(f"{base_url}/projects/{project_id}", json={"deleted": True})
