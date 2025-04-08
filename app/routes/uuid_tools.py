from fastapi import APIRouter
import uuid

router = APIRouter(prefix="/tools/uuid", tags=["UUID Tools"])

@router.get("/generate")
def generate_uuid():
    return {"uuid": str(uuid.uuid4())}
