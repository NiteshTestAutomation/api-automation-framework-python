import json
import allure
from utilities.assertions import assert_status_code, assert_json_key, validate_schema

@allure.feature("Login API")
@allure.title("Validate Login API returns token")

def test_login_api(client, base_url, login_payload):
    url = base_url + "/login"
    response = client.post(url, login_payload)

    assert_status_code(response, 200)
    assert_json_key(response, "token")

    with open("schemas/login_schema.json") as file:
        schema = json.load(file)

    validate_schema(response.json(), schema)
