from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import base64

# Creating a router with a prefix and a tag
router = APIRouter(prefix="/tools/base64", tags=["Base64 Tools"])

# Request model for encoding plain text
class Base64Input(BaseModel):
    content: str

# Request model for decoding Base64
@router.post("/encode")
def encode_base64(data: Base64Input):
    try:
        encoded = base64.b64encode(data.content.encode("utf-8")).decode("utf-8")
        return {"encoded": encoded}
    except Exception as e:
        raise HTTPException(status_code=400, detail="Failed to encode string to Base64.")

class Base64EncodedInput(BaseModel):
    encoded: str

@router.post("/decode")
def decode_base64(data: Base64EncodedInput):
    try:
        decoded_bytes = base64.b64decode(data.encoded.encode("utf-8"))
        decoded = decoded_bytes.decode("utf-8")
        return {"decoded": decoded}
    except Exception:
        raise HTTPException(status_code=400, detail="Failed to decode Base64 string.")

