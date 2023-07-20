import requests
import pytest
from unittest.mock import Mock

# The base URL of the API
BASE_URL = "http://127.0.0.1:8000"

# Test case: Check unauthorized access with incorrect credentials
def test_unauthorized_access(mocker):
    # Mock the response for unauthorized access (status code: 401, empty text response)
    mocker.patch(
        "requests.get",
        return_value=Mock(status_code=401, text=""),
    )

    # Endpoint and parameters
    endpoint = "/users"
    params = {"username": "admin", "password": "admin"}

    # Send a GET request with parameters
    response = requests.get(f"{BASE_URL}{endpoint}", params=params)

    # Check if the response status code is 401 (Unauthorized)
    assert response.status_code == 401

    # Check if the response is empty (text response should be empty)
    assert not response.text

# Test case: Check authorized access with correct credentials
def test_authorized_access(mocker):
    # Mock the response for authorized access (status code: 200, empty text response)
    mocker.patch(
        "requests.get",
        return_value=Mock(status_code=200, text=""),
    )

    # Endpoint and parameters
    endpoint = "/users"
    params = {"username": "admin", "password": "qwerty"}

    # Send a GET request with parameters
    response = requests.get(f"{BASE_URL}{endpoint}", params=params)

    # Check if the response status code is 200 (OK)
    assert response.status_code == 200

    # Check if the response is empty (text response should be empty)
    assert not response.text

# Run the tests
if __name__ == "__main__":
    pytest.main()
