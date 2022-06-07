from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_raiz_200():
    response = client.get("/api/raiz?numero=10")
    assert response.status_code == 200


def test_raiz_positivo():
    response = client.get("/api/raiz?numero=10")
    numero = 10
    resultado = str(numero ** (1/2))
    resultado_api = response.text
    assert resultado == resultado_api


def test_raiz_negativo():
    response = client.get("/api/raiz?numero=-10")
    assert response.status_code == 400
