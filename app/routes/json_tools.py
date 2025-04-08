from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
import json

# Create a FastAPI router with a URL prefix and tag for grouping
router = APIRouter(prefix="/tools/json", tags=["JSON Tools"])

# Request model for the JSON prettifier
class JSONPrettifyInput(BaseModel):
    content: str = Field(
        example='{"key":"value"}',
        description="Raw JSON string to be formatted"
    )

# Response model for the prettified JSON output
class JSONPrettifyResponse(BaseModel):
    prettified: str = Field(
        example='{\n    "key": "value"\n}',
        description="Formatted JSON string with proper indentation"
    )

@router.post(
    "/prettify",
    response_model=JSONPrettifyResponse,
    summary="Prettify a raw JSON string",
    response_description="Formatted JSON string with indentation"
)
def prettify_json(data: JSONPrettifyInput):
    """
    Convert a compact JSON string into a human-readable, formatted string.

    Parameters:
        data (JSONPrettifyInput): JSON payload containing raw JSON text.

    Returns:
        JSONPrettifyResponse: A dictionary with the prettified version of the input JSON.
    """
    try:
        # Parse the raw JSON string into a Python object
        parsed = json.loads(data.content)

        # Re-convert to JSON with indentation
        prettified = json.dumps(parsed, indent=4)

        return {"prettified": prettified}
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid JSON string.")

