import requests


base_url = "https://ru.yougile.com/api-v2"


def test_create_project(pro_id):
    payload = {
        "title": "Создание ДЗ",
        "user_id": "admin"},
    resp = requests.get(f"{base_url}/projects/{pro_id}")
    assert resp.status_code == 200, resp.text
    assert resp.json()["title"] == payload["title"]
    assert resp.json()['id'] == pro_id


def test_get_project(pro_id):
    resp = requests.get(f"{base_url}/projects/{pro_id}")
    assert resp.json()['id'] == pro_id


def test_delete_project(pro_id):
    payload = {"deleted": True, "title": "Создание ДЗ"}
    resp = requests.put(f"{base_url}/projects/{pro_id}", json=payload)
    assert resp.status_code == 200, resp.text
    assert resp.json()["id"] == pro_id
    got = requests.get(f"{base_url}/projects/{pro_id}")
    assert got.status_code == 200, got.text
    assert got.json()["deleted"] is True
