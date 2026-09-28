# helps.py
import allure
import requests

from endpoints import Endpoints
from urls import Urls
from data import DataCreateCourier


class Courier:
    """Класс для работы с API курьеров"""

    @staticmethod
    @allure.step('Регистрация курьера в системе')
    def courier_registration_in_the_system_and_get_courier_data():
        """Регистрация курьера и получение данных"""
        data = DataCreateCourier.generating_fake_valid_data_to_create_courier()
        response = requests.post(
            f'{Urls.QA_SCOOTER_URL}{Endpoints.create_courier}',
            data=data
        )
        return {
            "response_text": response.text,
            "status_code": response.status_code,
            "data": data
        }

    @staticmethod
    @allure.step('Авторизация курьера и получение ID')
    def courier_login_in_the_system_and_get_id_courier(data):
        """Логин курьера и получение ID"""
        response = requests.post(
            f'{Urls.QA_SCOOTER_URL}{Endpoints.login_courier}',
            data=data
        )
        return {
            "id": str(response.json()["id"]),
            "response_text": response.text,
            "status_code": response.status_code
        }

    @staticmethod
    @allure.step('Удаление курьера с ID: {id}')
    def courier_subsequent_deletion(id):
        """Удаление курьера по ID"""
        response = requests.delete(
            f'{Urls.QA_SCOOTER_URL}{Endpoints.delete_courier}{id}'
        )
        return {
            "response_text": response.text,
            "status_code": response.status_code
        }