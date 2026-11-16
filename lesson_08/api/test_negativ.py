base_url = "https://ru.yougile.com/api-v2"


def test_create_project(api_client):
    payload = {"title": "", "users": []}
    resp = api_client.post(f"{base_url}/projects", json=payload)
    assert resp.status_code == 400, resp.text


def test_get_project(api_client):
    resp = api_client.get(f"{base_url}/projects/enkrjvn43")
    assert resp.status_code == 404, resp.text


def test_delete_project(api_client):
    resp = api_client.put(f"{base_url}/projects/enkrjvn43", json={})
    assert resp.status_code == 404, resp.text
