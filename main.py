from fastapi import FastAPI


app = FastAPI()

@app.get("/")

def home():
    return {"message": "Welcome to FastAPI"}

@app.get("/hello")
def hello():
    return { "msg":"hello from server!"}


@app.put("/hello")
def hello():
    return {"msg":"hello from API"}


@app.post("/hello")
def hello():
    return {"msg":"Post from server"}


@app.patch("/hello")
def hello():
    return {"msg":"Patch from server"}