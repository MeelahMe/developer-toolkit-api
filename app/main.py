import time
import uuid
from fastapi import FastAPI, Request
from app.logging_config import setup_logging
from app.routes import json_tools, uuid_tools, base64_tools, time_tools, password_tools
from app.auth import verify_api_key
from fastapi import Depends
from app.metrics import REQUEST_COUNT, REQUEST_DURATION
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST
from fastapi import Response
from sqlalchemy.orm import Session
from app.database import SessionLocal, get_db
from app.models import RequestLog

logger = setup_logging()

app = FastAPI(
    title="Developer Toolkit API",
    description="A collection of backend utilities for developers including encoding, formatting, timestamp conversion, and more.",
    version="1.0.0",
    contact={
        "name": "Jameelah Mercer",
        "url": "https://www.linkedin.com/in/jameelahmercer/",
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

    duration_seconds = time.perf_counter() - start_time
    duration_ms = round(duration_seconds * 1000, 2)

    REQUEST_COUNT.labels(
        method=request.method,
        path=request.url.path,
        status_code=response.status_code,
    ).inc()
    REQUEST_DURATION.labels(
        method=request.method,
        path=request.url.path,
    ).observe(duration_seconds)

    db: Session = SessionLocal()
    try:
        db_log = RequestLog(
            method=request.method,
            path=request.url.path,
            status_code=response.status_code,
            duration_ms=duration_ms,
        )
        db.add(db_log)
        db.commit()
    finally:
        db.close()

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


@app.get("/metrics", tags=["Monitoring"])
def metrics():
    return Response(content=generate_latest(), media_type=CONTENT_TYPE_LATEST)


@app.get("/usage", tags=["Monitoring"], dependencies=[Depends(verify_api_key)])
def get_usage(limit: int = 50, db: Session = Depends(get_db)):
    logs = db.query(RequestLog).order_by(RequestLog.id.desc()).limit(limit).all()
    return [
        {
            "id": log.id,
            "timestamp": log.timestamp.isoformat(),
            "method": log.method,
            "path": log.path,
            "status_code": log.status_code,
            "duration_ms": log.duration_ms,
        }
        for log in logs
    ]


app.include_router(json_tools.router, dependencies=[Depends(verify_api_key)])
app.include_router(uuid_tools.router, dependencies=[Depends(verify_api_key)])
app.include_router(base64_tools.router, dependencies=[Depends(verify_api_key)])
app.include_router(time_tools.router, dependencies=[Depends(verify_api_key)])
app.include_router(password_tools.router, dependencies=[Depends(verify_api_key)])


@app.get("/", tags=["Root"])
def read_root():
    """
    Root endpoint that returns a welcome message.
    """
    return {"message": "Welcome to the Developer Toolkit API!"}
