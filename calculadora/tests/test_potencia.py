from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_potencia_200():
    response = client.get("/api/potencia?numero1=10&numero2=20")
    assert response.status_code == 200


def test_potencia_positivo():
    response = client.get("/api/potencia?numero1=10&numero2=2")
    numero1 = 10
    numero2 = 2
    resultado = str(numero1 ** numero2)
    resultado_api = response.text
    assert resultado == resultado_api


def test_potencia_negativo():
    response = client.get("/api/potencia?numero1=-10&numero2=3")
    numero1 = -10
    numero2 = 3
    resultado = str(numero1 ** numero2)
    resultado_api = response.text
    assert resultado == resultado_api