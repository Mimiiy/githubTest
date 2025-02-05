import pytest
import requests

#call the base url
def test_git_api ():
    query = "Python"
    base_url = f"https://api.github.com/search/users?q={query}"

    response = requests.get(base_url)
    if response.status_code == 200:
        formatted_text = response.json()
        print(f"{formatted_text}")
    else:
        print(f"unsuccessful query")