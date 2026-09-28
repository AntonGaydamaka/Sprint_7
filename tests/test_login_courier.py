import allure
import pytest
import requests
from data import DataCourier
from helps import Courier
from endpoints import Endpoints
from urls import Urls


class TestLoginCourier:

    @allure.title('Проверка авторизации курьера с валидными данными')
    @allure.description('Отправляем запрос на авторизацию в сервисе, проверяем ответ и удаляем курьера')
    def test_courier_login_success(self, courier):
        courier_data = courier
        response = Courier().courier_login_in_the_system_and_get_id_courier(courier_data["data"])
        
        assert response["status_code"] == 200, f"Expected 200, got {response['status_code']}"
        assert "id" in response, "Response doesn't contain 'id' field"
        assert response["id"], "ID is empty"

    @allure.title('Проверка ошибки при авторизации курьера без заполнения обязательных полей Login/Password')
    @allure.description('''Отправляем запрос на авторизацию в сервисе без заполнения обязательных полей Login/Password
                         и проверяем ответ''')
    @pytest.mark.parametrize('courier_data', [
        DataCourier.invalid_data_without_login,
        DataCourier.invalid_data_without_password
    ])
    def test_courier_login_without_parameters_failed(self, courier_data):
        response = requests.post(
            f'{Urls.QA_SCOOTER_URL}{Endpoints.login_courier}',
            json=courier_data
        )
        
        assert response.status_code == 400, f"Expected 400, got {response.status_code}"
        assert "Недостаточно данных для входа" in response.text, \
            f"Unexpected error message: {response.text}"

    @allure.title('Проверка ошибки при авторизации курьера с несуществующими данными')
    @allure.description('Отправляем запрос на авторизацию в сервисе с несуществующими данными и проверяем ответ')
    def test_courier_login_with_null_login_failed(self):
        response = requests.post(
            f'{Urls.QA_SCOOTER_URL}{Endpoints.login_courier}',
            json=DataCourier.null_data_login
        )
        
        assert response.status_code == 404, f"Expected 404, got {response.status_code}"
        assert "Учетная запись не найдена" in response.text, \
            f"Unexpected error message: {response.text}"

    @allure.title('Проверка ошибки при авторизации курьера с неверным паролем')
    @allure.description('Отправляем запрос на авторизацию с правильным логином, но неверным паролем')
    def test_courier_login_with_wrong_password_failed(self, courier):
        courier_data = courier["data"].copy()
        courier_data["password"] = "wrong_password_123"
        
        response = requests.post(
            f'{Urls.QA_SCOOTER_URL}{Endpoints.login_courier}',
            json={"login": courier_data["login"], "password": courier_data["password"]}
        )
        
        assert response.status_code == 404, f"Expected 404, got {response.status_code}"
        assert "Учетная запись не найдена" in response.text, \
            f"Unexpected error message: {response.text}"