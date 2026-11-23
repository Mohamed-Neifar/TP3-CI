from fastapi import FastAPI, HTTPException

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI TP3 - CI"}


@app.get("/addition")
def addition(a: int = 0, b: int = 0):
    return {
        "result a+b=": a + b
    }


@app.get("/greeting")
def greeting(name: str = "World"):
    return {
        "message": f"Hello, {name}!"
    }


@app.post("/multiply")
def multiply(a: int = 0, b: int = 0):
    return {
        "result a*b=": a * b
    }


@app.post("/divide")
def divide(a: float = 0, b: float = 1):
    if b == 0:
        raise HTTPException(status_code=400, detail="Division by zero is not allowed")
    return {
        "result a/b=": a / b
    }