from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def print_hello():
    return {"message": "Hello World"}

@app.get("/hello/{name}")
def get_name(name:str):
    return {"message" : f"hello {name}"}