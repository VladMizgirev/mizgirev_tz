# https://petstore.swagger.io/#/

import requests

headers = {
    'Content-type': 'application/json',
    'Accept': 'application/json',
    'api_key': '12334443'
}


def add_users():
    data = [{
        "id": 1,
        "username": "Vlad1",
        "firstName": "Vlad",
        "lastName": "Mizgirev",
        "email": "vlad@mail.ru",
        "password": "123",
        "phone": "8976",
        "userStatus": 0
    }, {
        "id": 2,
        "username": "Islam",
        "firstName": "Islam",
        "lastName": "Vorokov",
        "email": "islam@mail.ru",
        "password": "123",
        "phone": "8976",
        "userStatus": 0
    }]

    response = requests.post("https://petstore.swagger.io/v2/user/createWithList/", json=data, headers=headers)
    return response


def get_info_by_username(username):
    response = requests.get(f"https://petstore.swagger.io/v2/user/{username}", headers=headers)
    return response.text


add_users()

print(get_info_by_username("Vlad1"))
print("------------------------------------------------------------")
print(get_info_by_username("Islam"))
