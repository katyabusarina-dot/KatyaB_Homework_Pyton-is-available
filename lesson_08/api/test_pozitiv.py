
base_url = "https://ru.yougile.com/api-v2"


def test_create_project(pro_id, api_client):
    resp = api_client.get(f"{base_url}/projects/{pro_id}")
    assert resp.status_code == 200, resp.text
    assert resp.json()["title"] == "Создание ДЗ"


def test_get_project(pro_id, api_client):
    resp = api_client.get(f"{base_url}/projects/{pro_id}")
    assert resp.json()['id'] == pro_id


def test_delete_project(pro_id, api_client):
    payload = {"deleted": True, "title": "Создание ДЗ"}
    resp = api_client.put(f"{base_url}/projects/{pro_id}", json=payload)
    assert resp.status_code == 200, resp.text
    assert resp.json()["id"] == pro_id
    got = api_client.get(f"{base_url}/projects/{pro_id}")
    assert got.status_code == 200, got.text
    assert got.json()["deleted"] is True
