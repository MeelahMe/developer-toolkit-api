from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import base64

router = APIRouter(prefix="/tools/base64", tags=["Base64 Tools"])

class Base64Input(BaseModel):
    content: str

@router.post("/encode")
def encode_base64(data: Base64Input):
    try:
        encoded = base64.b64encode(data.content.encode("utf-8")).decode("utf-8")
        return {"encoded": encoded}
    except Exception as e:
        raise HTTPException(status_code=400, detail="Failed to encode string to Base64.")

