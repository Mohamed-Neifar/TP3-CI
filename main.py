"""FastAPI application for TP3 Continuous Integration."""

from fastapi import FastAPI, HTTPException

app = FastAPI()


@app.get("/")
def read_root():
    """Return a welcome message."""
    return {"message": "Welcome to FastAPI TP3 - CI"}


@app.get("/addition")
def addition(a: int = 0, b: int = 0):
    """Return the sum of two integers."""
    return {
        "result a+b=": a + b
    }


@app.get("/soustraction")
def soustraction(a: int = 0, b: int = 0):
    """Return the difference between two integers."""
    return {
        "result a-b=": a - b
    }


@app.get("/greeting")
def greeting(name: str = "World"):
    """Return a personalized greeting message."""
    return {
        "message": f"Hello, {name}!"
    }


@app.post("/multiply")
def multiply(a: int = 0, b: int = 0):
    """Return the product of two integers."""
    return {
        "result a*b=": a * b
    }


@app.post("/divide")
def divide(a: float = 0, b: float = 1):
    """Return the quotient of two numbers, raising HTTP 400 on division by zero."""
    if b == 0:
        raise HTTPException(status_code=400, detail="Division by zero is not allowed")
    return {
        "result a/b=": a / b
    }
