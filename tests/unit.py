import pytest
from unittest.mock import patch, MagicMock
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

# Тесты для функции root
def test_root_return_valid_json():
    response = client.get("/")
    assert response.status_code == 200
    assert "info" in response.json()
    assert "id" in response.json()

def test_root_handles_no_recepts_found():
    with patch('main.random.randint') as mock_randint, \
         patch('main.requests.get') as mock_get:
        # Создаем заглушки для обработки случая, когда рецепты не найдены
        id = -1
        mock_randint.return_value = id
        mock_get.return_value.json.return_value = {}

        response = client.get("/")
        assert response.status_code == 404
        assert response.json() == {"detail": "No recipes found"}

# Тесты для функции get_list
def test_get_list():
    response = client.get("/list/?q=123")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_list_returns_expected_recepts():
    with patch('main.requests.get') as mock_get:
        # Создаем заглушку для get, чтобы возвращать фиксированный результат
        mock_recepts = MagicMock()
        mock_recepts.json.return_value = {'title': 'Tart Green Salad with Avocado Dressing'}
        mock_get.return_value = mock_recepts

        response = client.get("/list/?q=123")
        assert response.status_code == 200
        assert response.json() == [{'id': '123', 'info': {'title': 'Tart Green Salad with Avocado Dressing'}}]
