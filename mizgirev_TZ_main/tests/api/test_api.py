import json
import random
import allure


class TestApi:

    @allure.description("Регистрация пользователя и получение данных")
    def test_get_add_user_and_get_info(self, api_client, test_data):
        person_random = test_data.get_random_person()
        api_client.add_users(person_random)
        info = json.loads(api_client.get_info_by_username(person_random[0]['username']))
        assert person_random[0]['firstName'] == info['firstName']

    @allure.description("Редактирование данных пользователя")
    def test_change_user_data(self, api_client, test_data):
        new_email = f"{random.randint(10000, 99999)}@yandex.ru"
        person_random = test_data.get_random_person()
        api_client.add_users(person_random)
        info = json.loads(api_client.get_info_by_username(username=person_random[0]['username']))
        assert person_random[0]['firstName'] == info['firstName']

        person_random[0]["email"] = new_email
        api_client.change_user_info(username=person_random[0]['username'], data=person_random[0])
        info = json.loads(api_client.get_info_by_username(username=person_random[0]['username']))
        assert new_email == info['email']

    @allure.description("Удаление пользователя")
    def test_delete_user(self, api_client, test_data):
        person_random = test_data.get_random_person()
        api_client.add_users(person_random)
        info = json.loads(api_client.get_info_by_username(person_random[0]['username']))
        assert person_random[0]['firstName'] == info['firstName']

        api_client.delete_user(person_random[0]['username'])
        info = json.loads(api_client.get_info_by_username(person_random[0]['username']))
        assert info["message"] == 'User not found'
