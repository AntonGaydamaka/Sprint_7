from generators import DataCreateCourier


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