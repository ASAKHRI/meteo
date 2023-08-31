from req_api import city, weather
import pytest
import requests


# Utilisation de pytest pour mocker les appels réseau
@pytest.fixture
def mock_requests_get_city(monkeypatch):
    class MockResponse:
        def json(self):
            return [{"lat": 45.75, "lon": 4.85}]

    def mock_get(*args, **kwargs):
        return MockResponse()

    monkeypatch.setattr(requests, 'get', mock_get)

@pytest.fixture
def mock_requests_get_weather(monkeypatch):
    class MockResponse:
        def json(self):
            return {"weather": [{"main": "Clear", "description": "clear sky"}]}

    def mock_get(*args, **kwargs):
        return MockResponse()

    monkeypatch.setattr(requests, 'get', mock_get)

def test_city(mock_requests_get_city):
    result = city()
    assert result == [{"lat": 45.75, "lon": 4.85}]

def test_weather(mock_requests_get_weather):
    result = weather()
    assert result == {"weather": [{"main": "Clear", "description": "clear sky"}]}
