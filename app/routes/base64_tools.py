from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
import base64

router = APIRouter(prefix="/tools/base64", tags=["Base64 Tools"])

# Input model for encoding plain text
class Base64EncodeInput(BaseModel):
    content: str = Field(
        example="hello world",
        description="The plain text string to encode into Base64"
    )

# Output model for encoded result
class Base64EncodeResponse(BaseModel):
    encoded: str = Field(
        example="aGVsbG8gd29ybGQ=",
        description="The Base64-encoded string"
    )

# Input model for decoding Base64 string
class Base64DecodeInput(BaseModel):
    encoded: str = Field(
        example="aGVsbG8gd29ybGQ=",
        description="The Base64-encoded string to decode"
    )

# Output model for decoded result
class Base64DecodeResponse(BaseModel):
    decoded: str = Field(
        example="hello world",
        description="The decoded plain text string"
    )

@router.post(
    "/encode",
    response_model=Base64EncodeResponse,
    summary="Encode a string to Base64",
    response_description="Returns the Base64-encoded version of the input"
)
def encode_base64(data: Base64EncodeInput):
    """
    Encode a plain text string into Base64.

    Accepts a `content` field containing a UTF-8 string,
    and returns its Base64-encoded version.
    """
    try:
        encoded = base64.b64encode(data.content.encode("utf-8")).decode("utf-8")
        return {"encoded": encoded}
    except Exception:
        raise HTTPException(status_code=400, detail="Failed to encode string to Base64.")

@router.post(
    "/decode",
    response_model=Base64DecodeResponse,
    summary="Decode a Base64 string to plain text",
    response_description="Returns the decoded string"
)
def decode_base64(data: Base64DecodeInput):
    """
    Decode a Base64 string back into plain text.

    Accepts an `encoded` field containing a Base64 string,
    and returns the decoded UTF-8 string.
    """
    try:
        decoded_bytes = base64.b64decode(data.encoded.encode("utf-8"))
        decoded = decoded_bytes.decode("utf-8")
        return {"decoded": decoded}
    except Exception:
        raise HTTPException(status_code=400, detail="Failed to decode Base64 string.")
