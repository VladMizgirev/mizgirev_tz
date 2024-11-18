import requests


class ApiClient:
    def __init__(self):
        self.__headers = {
            'Content-type': 'application/json',
            'Accept': 'application/json',
            'api_key': '12334443'
        }
        self.__url = "https://petstore.swagger.io/v2/"

    def add_users(self, data: list):
        response = requests.post(self.__url + 'user/createWithList/', json=data, headers=self.__headers)
        return response.text

    def get_info_by_username(self, username: str):
        response = requests.get(self.__url + f"user/{username}", headers=self.__headers)
        return response.text


    def change_user_info(self, username, data: dict):
        response = requests.put(self.__url + f"user/{username}", json= data, headers=self.__headers)
        return response.text

    def delete_user(self, username):
        response = requests.delete(self.__url + f"user/{username}", headers=self.__headers)
        return response.text