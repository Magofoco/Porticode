import requests


def get_info_from_api(i):
    ISBN = 9780140361216 - i
    str_isbn = str(ISBN)
    api_base_url = "https://openlibrary.org/api/books?bibkeys=ISBN:" + str_isbn + "&jscmd=data&format=json"
    response = requests.get(api_base_url)
    response.raise_for_status()
    response = response.json()
    return response, str_isbn
