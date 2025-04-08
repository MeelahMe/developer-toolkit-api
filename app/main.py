from fastapi import FastAPI
from app.routes import (
    json_tools,
    uuid_tools,
    base64_tools,
    time_tools,
    password_tools
)

# Initialize the FastAPI app with metadata for documentation
app = FastAPI(
    title="Developer Toolkit API",
    description="A collection of backend utilities for developers including encoding, formatting, timestamp conversion, and more.",
    version="1.0.0",
    contact={
        "name": "Jameelah Mercer",
        "email": "hello@juadocs.com",
        "url": "https://juadocs.com"
    },
    license_info={
        "name": "MIT",
        "url": "https://opensource.org/licenses/MIT",
    },
)

# Register routers for each toolkit module
app.include_router(json_tools.router)
app.include_router(uuid_tools.router)
app.include_router(base64_tools.router)
app.include_router(time_tools.router)
app.include_router(password_tools.router)

# Root route to verify the API is running
@app.get("/", tags=["Root"])
def read_root():
    """
    Root endpoint that returns a welcome message.
    """
    return {"message": "Welcome to the Developer Toolkit API!"}

