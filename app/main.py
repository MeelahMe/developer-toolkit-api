from fastapi import FastAPI
from app.routes import json_tools

app = FastAPI(title="Developer Toolkit API")

app.include_router(json_tools.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Developer Toolkit API!"}

