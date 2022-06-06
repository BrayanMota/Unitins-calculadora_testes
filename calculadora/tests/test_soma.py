from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_soma():
    response = client.get("/api/adicao?numero1=10&numero2=20")
    assert response.status_code == 200
    assert response == {"Resultado da Soma": "30"}