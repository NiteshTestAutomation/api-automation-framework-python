import json
import pytest
from utilities.api_client import APIClient
from utilities.config_reader import get_base_url

@pytest.fixture(scope="session")
def client():
    return APIClient()

@pytest.fixture(scope="session")
def base_url():
    return get_base_url()

@pytest.fixture
def login_payload():
    with open("payloads/login_payload.json") as file:
        return json.load(file)

@pytest.fixture
def transfer_payload():
    with open("payloads/transfer_payload.json") as file:
        return json.load(file)
