import json
import pytest
import os
from utilities.api_client import APIClient
from utilities.config_reader import get_base_url, get_object_base_url


@pytest.fixture(scope="session")
def client():
    return APIClient()

@pytest.fixture(scope="session")
def base_url():
    return get_base_url()

@pytest.fixture(scope="session")
def object_base_url():
    return get_object_base_url()


@pytest.fixture
def login_payload():
    with open("payloads/login_payload.json") as file:
        return json.load(file)

@pytest.fixture
def transfer_payload():
    with open("payloads/transfer_payload.json") as file:
        return json.load(file)

@pytest.fixture
def addObject_payload():
    base_dir = os.path.dirname(os.path.abspath(__file__))  # conftest.py location
    file_path = os.path.join(base_dir, "payloads", "add_object_payload.json")
    with open(file_path) as file:
        return json.load(file)


@pytest.fixture
def updateObject_payload():
    base_dir = os.path.dirname(os.path.abspath(__file__))  # conftest.py location
    file_path = os.path.join(base_dir, "payloads", "update_object_payload.json")
    with open(file_path) as file:
        return json.load(file)