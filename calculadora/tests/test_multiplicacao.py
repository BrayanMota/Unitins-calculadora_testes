from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_multiplicacao_200():
    response = client.get("/api/multiplicacao?numero1=10&numero2=20")
    assert response.status_code == 200


def test_multiplicacao_positivo():
    response = client.get("/api/multiplicacao?numero1=10&numero2=20")
    numero1 = 10
    numero2 = 20
    resultado = str(numero1 * numero2)
    resultado_api = response.text
    assert resultado == resultado_api


def test_multiplicacao_negativo():
    response = client.get("/api/multiplicacao?numero1=10&numero2=-20")
    numero1 = 10
    numero2 = -20
    resultado = str(numero1 * numero2)
    resultado_api = response.text
    assert resultado == resultado_api