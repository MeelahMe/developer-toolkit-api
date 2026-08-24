import time
import uuid
from fastapi import FastAPI, Request
from app.logging_config import setup_logging
from app.routes import json_tools, uuid_tools, base64_tools, time_tools, password_tools

logger = setup_logging()

app = FastAPI(
    title="Developer Toolkit API",
    description="A collection of backend utilities for developers including encoding, formatting, timestamp conversion, and more.",
    version="1.0.0",
    contact={
        "name": "Jameelah Mercer",
        "email": "hello@juadocs.com",
        "url": "https://juadocs.com",
    },
    license_info={
        "name": "MIT",
        "url": "https://opensource.org/licenses/MIT",
    },
)


@app.middleware("http")
async def log_requests(request: Request, call_next):
    request_id = str(uuid.uuid4())
    start_time = time.perf_counter()

    response = await call_next(request)

    duration_ms = round((time.perf_counter() - start_time) * 1000, 2)

    logger.info(
        "request_handled",
        extra={
            "request_id": request_id,
            "method": request.method,
            "path": request.url.path,
            "status_code": response.status_code,
            "duration_ms": duration_ms,
        },
    )

    response.headers["X-Request-ID"] = request_id
    return response


app.include_router(json_tools.router)
app.include_router(uuid_tools.router)
app.include_router(base64_tools.router)
app.include_router(time_tools.router)
app.include_router(password_tools.router)


@app.get("/", tags=["Root"])
def read_root():
    """
    Root endpoint that returns a welcome message.
    """
    return {"message": "Welcome to the Developer Toolkit API!"}
