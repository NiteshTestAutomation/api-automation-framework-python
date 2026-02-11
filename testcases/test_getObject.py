from utilities.api_client import APIClient
from utilities.config_reader import get_base_url
from utilities.config_reader import get_object_base_url

def test_getListOfobj_api():
    client = APIClient()
    url = get_object_base_url() + "objects"

    response = client.get(url)

    assert response.status_code == 200
    # assert "token" in response.json()
