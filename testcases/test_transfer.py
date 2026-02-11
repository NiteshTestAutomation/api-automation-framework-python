import allure
from utilities.assertions import assert_status_code, assert_json_key

@allure.feature("Transfer API")
@allure.title("Validate Transfer API creates user")
def test_transfer_api(client, base_url, transfer_payload):

    url = base_url + "/users"
    response = client.post(url, transfer_payload)

    assert_status_code(response, 201)
    assert_json_key(response, "id")
    assert_json_key(response, "createdAt")
