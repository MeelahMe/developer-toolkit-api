from fastapi import FastAPI
from app.routes import json_tools, uuid_tools, base64_tools, time_tools, password_tools

app = FastAPI(title="Developer Toolkit API")

app.include_router(json_tools.router)
app.include_router(uuid_tools.router)
app.include_router(base64_tools.router)
app.include_router(time_tools.router)
app.include_router(password_tools.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Developer Toolkit API!"}

