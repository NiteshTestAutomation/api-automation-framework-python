from utilities.api_client import APIClient
from utilities.config_reader import get_base_url

def test_login_api():
    client = APIClient()
    url = get_base_url() + "/login"

    payload = {
        "username": "admin",
        "password": "admin123"
    }

    response = client.post(url, payload)

    assert response.status_code == 200
    assert "token" in response.json()
