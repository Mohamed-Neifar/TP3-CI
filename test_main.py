"""Unit tests for the FastAPI application endpoints."""

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_root():
    """Test the root endpoint."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to FastAPI TP3 - CI"}


def test_addition():
    """Test the addition endpoint."""
    response = client.get("/addition?a=5&b=3")
    assert response.status_code == 200
    assert response.json() == {"result a+b=": 8}


def test_soustraction():
    """Test the subtraction endpoint."""
    response = client.get("/soustraction?a=10&b=4")
    assert response.status_code == 200
    assert response.json() == {"result a-b=": 6}


def test_greeting():
    """Test the greeting endpoint."""
    response = client.get("/greeting?name=Mohamed")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, Mohamed!"}


def test_multiply():
    """Test the multiplication endpoint."""
    response = client.post("/multiply?a=4&b=5")
    assert response.status_code == 200
    assert response.json() == {"result a*b=": 20}


def test_divide():
    """Test the division endpoint."""
    response = client.post("/divide?a=10&b=2")
    assert response.status_code == 200
    assert response.json() == {"result a/b=": 5.0}


def test_divide_by_zero():
    """Test the division by zero error handling."""
    response = client.post("/divide?a=10&b=0")
    assert response.status_code == 400
    assert response.json() == {"detail": "Division by zero is not allowed"}
