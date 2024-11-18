from faker import Faker
import random


class PersonDataGenerate:
    def __init__(self):
        self.fake = Faker()

    def get_random_person(self):
        """
        Создание и получение рандомного пользователя
        :return:
        """
        username = self.fake.user_name()
        password = self.fake.password()
        email = self.fake.email()
        phone = self.fake.phone_number()
        fake_person = {
            'id': random.randint(1000000000000, 9999999999999),
            'username': username,
            "firstName": "Vlad",
            "lastName": "Mizgirev",
            'password': password,
            'email': email,
            "phone": phone,
            "userStatus": 0
        }
        return [fake_person]
