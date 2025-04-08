from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
import base64

# Create a router for Base64 encoding/decoding routes
router = APIRouter(prefix="/tools/base64", tags=["Base64 Tools"])

# Request model for encoding input
class Base64EncodeInput(BaseModel):
    content: str = Field(
        example="hello world",
        description="The plain text string to encode into Base64"
    )

# Response model for encoded result
class Base64EncodeResponse(BaseModel):
    encoded: str = Field(
        example="aGVsbG8gd29ybGQ=",
        description="The Base64-encoded output string"
    )

# Request model for decoding input
class Base64DecodeInput(BaseModel):
    encoded: str = Field(
        example="aGVsbG8gd29ybGQ=",
        description="The Base64-encoded string to decode"
    )

# Response model for decoded result
class Base64DecodeResponse(BaseModel):
    decoded: str = Field(
        example="hello world",
        description="The decoded plain text string"
    )

@router.post(
    "/encode",
    response_model=Base64EncodeResponse,
    summary="Encode a string to Base64",
    response_description="Returns the Base64-encoded result"
)
def encode_base64(data: Base64EncodeInput):
    """
    Encode a plain text string into Base64 format.

    Parameters:
        data (Base64EncodeInput): JSON object with a 'content' field.

    Returns:
        Base64EncodeResponse: Encoded Base64 string.
    """
    try:
        encoded = base64.b64encode(data.content.encode("utf-8")).decode("utf-8")
        return {"encoded": encoded}
    except Exception:
        raise HTTPException(status_code=400, detail="Failed to encode string to Base64.")

@router.post(
    "/decode",
    response_model=Base64DecodeResponse,
    summary="Decode a Base64 string",
    response_description="Returns the decoded plain text result"
)
def decode_base64(data: Base64DecodeInput):
    """
    Decode a Base64 string into a plain UTF-8 string.

    Parameters:
        data (Base64DecodeInput): JSON object with an 'encoded' field.

    Returns:
        Base64DecodeResponse: Decoded plain text string.
    """
    try:
        decoded_bytes = base64.b64decode(data.encoded.encode("utf-8"))
        decoded = decoded_bytes.decode("utf-8")
        return {"decoded": decoded}
    except Exception:
        raise HTTPException(status_code=400, detail="Failed to decode Base64 string.")
