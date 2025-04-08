from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
import json

router = APIRouter(prefix="/tools/json", tags=["JSON Tools"])

# Request model with a raw JSON string input
class JSONPrettifyInput(BaseModel):
    content: str = Field(
        example='{"key":"value"}',
        description="Raw JSON string to format"
    )

# Response model with prettified output
class JSONPrettifyResponse(BaseModel):
    prettified: str = Field(
        example='{\n    "key": "value"\n}',
        description="Formatted JSON string with indentation"
    )

@router.post(
    "/prettify",
    response_model=JSONPrettifyResponse,
    summary="Prettify a raw JSON string",
    response_description="Formatted JSON string with indentation"
)
def prettify_json(data: JSONPrettifyInput):
    """
    Prettify (beautify) a raw JSON string.

    Accepts a compact JSON string and returns a formatted version
    with indentation and line breaks.

    Returns:
        JSON object containing a single `prettified` key with the formatted string.
    """
    try:
        # Parse the input JSON string to an object
        parsed = json.loads(data.content)

        # Convert it back to a nicely indented string
        prettified = json.dumps(parsed, indent=4)

        return {"prettified": prettified}
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid JSON string.")

