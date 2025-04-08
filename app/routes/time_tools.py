from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from typing import Optional
from typing import Union
from datetime import datetime


router = APIRouter(prefix="/tools/time", tags=["Time Tools"])

# Input model that accepts either a timestamp or a date string
class TimeConversionInput(BaseModel):
    timestamp: Optional[int] = Field(
        default=None,
        example=1609459200,
        description="UNIX timestamp (optional)"
    )
    date_string: Optional[str] = Field(
        default=None,
        example="2021-01-01T00:00:00",
        description="ISO 8601 date string (optional)"
    )

# Response model when converting to timestamp
class TimestampResponse(BaseModel):
    timestamp: int

# Response model when converting to date string
class DateStringResponse(BaseModel):
    date_string: str

@router.post(
    "/convert",
    response_model=Union[TimestampResponse, DateStringResponse],
    summary="Convert between timestamp and date string",
    response_description="Returns either a timestamp or a formatted date string"
)
def convert_time(data: TimeConversionInput):
    """
    Convert between UNIX timestamps and ISO 8601 date strings.

    You must provide either a `timestamp` or a `date_string`.

    - If `timestamp` is provided, the response will include a `date_string`.
    - If `date_string` is provided, the response will include a `timestamp`.

    Returns:
        JSON object with the converted value.
    """
    try:
        if data.timestamp is not None:
            dt = datetime.fromtimestamp(data.timestamp)
            return {"date_string": dt.isoformat()}

        elif data.date_string is not None:
            dt = datetime.fromisoformat(data.date_string)
            return {"timestamp": int(dt.timestamp())}

        else:
            raise HTTPException(
                status_code=400,
                detail="Provide either 'timestamp' or 'date_string'."
            )
    except Exception:
        raise HTTPException(
            status_code=400,
            detail="Invalid input. Use a valid UNIX timestamp or ISO 8601 date string."
        )
