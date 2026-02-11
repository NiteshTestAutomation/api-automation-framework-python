from jsonschema import validate

def assert_status_code(response, expected):
    assert response.status_code == expected, f"Expected {expected}, but got {response.status_code}"

def assert_json_key(response, key):
    json_data = response.json()
    assert key in json_data, f"Key '{key}' not found in response"

def validate_schema(response_json, schema):
    validate(instance=response_json, schema=schema)
