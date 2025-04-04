from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import json

router = APIRouter(prefix="/tools/json", tags=["JSON Tools"])

class JsonInput(BaseModel):
    content: str

@router.post("/prettify")
def prettify_json(data: JsonInput):
    try:
        parsed = json.loads(data.content)
        pretty = json.dumps(parsed, indent=4)
        return {"prettified": pretty}
    except json.JSONDecodeError:
        raise HTTPException(status_code=400, detail="Invalid JSON input.")

