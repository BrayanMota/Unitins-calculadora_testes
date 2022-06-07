from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_fatorial_200():
    response = client.get("/api/fatorial?numero=10")
    assert response.status_code == 200


def test_fatorial_positivo():
    response = client.get("/api/fatorial?numero=10")
    numero = 10
    resultado = 1
    for i in range(1, numero + 1):
        resultado *= i
    resultado_str = str(resultado)
    resultado_api = response.text
    assert resultado_str == resultado_api


def test_fatorial_negativo():
    response = client.get("/api/fatorial?numero=-10")
    assert response.status_code == 400


def test_fatorial_0():
    response = client.get("/api/fatorial?numero=0")
    assert response.text == '1'
