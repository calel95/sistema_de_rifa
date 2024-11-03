from fastapi import FastAPI
from fastapi.testclient import TestClient
from .main import app

app = FastAPI()

client = TestClient(app)



def test_read_all_registers():
    response = client.get("/numeros/")
    assert response.status_code == 200
    assert response.json() == { "numero": 0, "nome": "string" }
