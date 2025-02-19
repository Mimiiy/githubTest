import pytest
import requests
import unittest.mock as mock

#manual testing
def test_git_api ():
    query = "Python"
    base_url = f"https://api.github.com/search/users?q={query}"
    response = requests.get(base_url)
    
    if response.status_code == 200:
        formatted_text = response.json()
        print(f"{formatted_text}")
    else:
        print(f"unsuccessful query")

def get_users():
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    if response.status_code == 200:
        return response.json()
    else:
        raise requests.HTTPError

#unit testing
@mock.patch("requests.get")    
def test_get_users_successful(mock_get):
    mock_response = mock.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"id": 1, "name": "Maryam"}
    mock_get.return_value = mock_response
    data = get_users()
    assert data == {"id": 1, "name": "Maryam"}

#This section is testing the for an unsuccessful API call
@mock.patch("requests.get")
def test_get_users_error(mock_get):
    mock_response = mock.Mock()
    mock_response.status_code = 000
    mock_get.return_value = mock_response
    with pytest.raises(requests.HTTPError):
        get_users()

