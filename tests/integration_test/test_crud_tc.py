from src.constants.api_constants import url, base_url, API_Constants


def test_crud():
    print(url)

    a = base_url()
    print(a)

    b = API_Constants.base_url()
    print(b)
