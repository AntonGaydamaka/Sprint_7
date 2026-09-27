# data.py
from faker import Faker


class DataCreateCourier:
    """Класс для генерации тестовых данных курьера"""
    
    @staticmethod
    def generating_fake_valid_data_to_create_courier():
        """Генерация валидных данных курьера"""
        fake = Faker("ru_RU")
        return {
            "login": fake.user_name(),
            "firstName": fake.first_name(),
            "password": fake.password()
        }

    @staticmethod
    def generating_fake_invalid_data_without_login():
        """Генерация данных без поля login"""
        fake = Faker("ru_RU")
        return {
            "login": "",
            "firstName": fake.first_name(),
            "password": fake.password()
        }

    @staticmethod
    def generating_fake_invalid_data_without_password():
        """Генерация данных без поля password"""
        fake = Faker("ru_RU")
        return {
            "login": fake.user_name(),
            "password": "",
            "firstName": fake.first_name()
        }


class DataCourier:
    """Подготовленные наборы данных для тестов"""
    
    valid_data_login = DataCreateCourier.generating_fake_valid_data_to_create_courier()
    invalid_data_without_login = DataCreateCourier.generating_fake_invalid_data_without_login()
    invalid_data_without_password = DataCreateCourier.generating_fake_invalid_data_without_password()
    
    null_data_login = {
        "login": "test",
        "password": "test"
    }


class DataOrder:
    """Данные для заказов"""
    
    data = {
        "firstName": "Антон",
        "lastName": "Гайдамака",
        "address": "г.Новороссийск",
        "metroStation": 1,
        "phone": "+7 800 000 0000",
        "rentTime": 4,
        "deliveryDate": "2026-09-15",
        "comment": "Хочу быстрее кататься!",
    }