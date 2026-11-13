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


@pytest.fixture
def pro_id():
    resp = requests.post(f"{base_url}/projects", json=payload)
    assert resp.status_code == 201
    project_id = resp.json()["id"]
    yield project_id
    requests.delete(f"{base_url}/projects/{project_id}")


def test_cpeate_project(pro_id):
    payload = {
        "title": "Создание ДЗ",
        "users": {
            user_id: {"role": "admin"}}}
    resp = requests.get(f"{base_url}/projects/{pro_id}")
    assert resp.status_code == 200, resp.text
    assert resp.json()["title"] == payload["title"]
    assert resp['id'] == pro_id


def test_delete_project(pro_id):
    payload = {"deleted": True, "title": "Создание ДЗ"}
    resp = requests.put(f"{base_url}/projects/{pro_id}", json=payload)
    assert resp.status_code == 200, resp.text
    assert resp.json()["id"] == pro_id
    got = requests.get(f"{base_url}/projects/{pro_id}")
    assert got.status_code == 200, got.text
    assert got.json()["deleted"] is True


def test_get_project(pro_id):
    resp = requests.get(f"{base_url}/projects/{pro_id}")
    assert resp['id'] == pro_id
    assert resp.status_code == 404
