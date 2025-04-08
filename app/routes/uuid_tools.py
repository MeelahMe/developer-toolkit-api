from fastapi import APIRouter
from pydantic import BaseModel, Field
import uuid

# Create a router with a URL prefix and grouping tag
router = APIRouter(prefix="/tools/uuid", tags=["UUID Tools"])

# Response model for the UUID generator
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
    Generate a version 4 (random) UUID.

    Returns:
        UUIDResponse: A dictionary containing the generated UUID.
    """
    return {"uuid": str(uuid.uuid4())}

