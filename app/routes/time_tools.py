from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from datetime import datetime

router = APIRouter(prefix="/tools/time", tags=["Time Tools"])

class TimeConversionInput(BaseModel):
    timestamp: int | None = None  # Optional UNIX timestamp input
    date_string: str | None = None  # Optional human-readable date string (ISO format)

@router.post("/convert")
def convert_time(data: TimeConversionInput):
    """
    Convert between UNIX timestamps and human-readable ISO 8601 date strings.
    
    - If `timestamp` is provided, returns a `date_string`
    - If `date_string` is provided, returns a `timestamp`

    Returns:
        JSON object with the converted value.
    """
    try:
        if data.timestamp is not None:
            # Convert UNIX timestamp to ISO 8601 date string
            dt = datetime.fromtimestamp(data.timestamp)
            return {"date_string": dt.isoformat()}

        elif data.date_string is not None:
            # Convert ISO 8601 date string to UNIX timestamp
            dt = datetime.fromisoformat(data.date_string)
            return {"timestamp": int(dt.timestamp())}

        else:
            raise HTTPException(status_code=400, detail="Provide either 'timestamp' or 'date_string'.")
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid input. Use a UNIX timestamp or an ISO date string.")

