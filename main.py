from fastapi import FastAPI

app = FastAPI()# app_name -> creating instace of FastAPI

@app.get('/')#action

def index(): #decorator
    return {'message': 'Hello, Fast API!'}