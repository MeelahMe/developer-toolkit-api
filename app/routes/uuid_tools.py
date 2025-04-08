from fastapi import APIRouter
from pydantic import BaseModel, Field
import uuid

router = APIRouter(prefix="/tools/uuid", tags=["UUID Tools"])

# Response model with example UUID
class UUIDResponse(BaseModel):
    uuid: str = Field(
        example="123e4567-e89b-12d3-a456-426614174000",
        description="Randomly generated UUID version 4"
    )

@router.get(
    "/generate",
    response_model=UUIDResponse,
    summary="Generate a UUID v4",
    response_description="A new random UUID"
)
def generate_uuid():
    """
    Generate a random UUID version 4.

    Returns:
        A JSON object containing a stringified UUID.
    """
    return {"uuid": str(uuid.uuid4())}

