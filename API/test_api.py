import pytest
import requests
import unittest.mock as mock
import api


#positive repsonse code
@pytest.mark.parametrize("url, response_code", [("https://api.github.com/search/users?q={Python}", 200), 
                                 ("https://fakerestapi.azurewebsites.net/api/v1/Activities",200),
                                 ("https://jsonplaceholder.typicode.com/users", 200)]
                         )
def test_get_api(url, response_code):
    response = requests.get(url)
    assert response.status_code == response_code


#unit testing
#This section tests for a successful API call
@mock.patch("requests.get")    
def test_get_users_successful(mock_get):
    mock_response = mock.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"id": 1, "name": "Maryam"}
    mock_get.return_value = mock_response
    data = api.get_users()
    assert data == {"id": 1, "name": "Maryam"}

#This section tests for an unsuccessful API call
@mock.patch("requests.get")
def test_get_users_error(mock_get):
    mock_response = mock.Mock()
    mock_response.status_code = 000
    mock_get.return_value = mock_response
    with pytest.raises(requests.HTTPError):
        api.get_users()

