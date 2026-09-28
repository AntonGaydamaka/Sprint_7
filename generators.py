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