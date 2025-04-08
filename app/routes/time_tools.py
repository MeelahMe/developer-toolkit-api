from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from typing import Optional, Union
from datetime import datetime, timezone

# Create a router for all time-related tools
router = APIRouter(prefix="/tools/time", tags=["Time Tools"])

# Input model: user can provide either a timestamp or a date string
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

# Output model when converting to timestamp
class TimestampResponse(BaseModel):
    timestamp: int

# Output model when converting to date string
class DateStringResponse(BaseModel):
    date_string: str

@router.post(
    "/convert",
    response_model=Union[TimestampResponse, DateStringResponse],
    summary="Convert between timestamp and date string",
    response_description="Returns either a timestamp or an ISO 8601 date string"
)
def convert_time(data: TimeConversionInput):
    """
    Convert between a UNIX timestamp and an ISO 8601 date string (UTC-based).

    You must provide either:
    - `timestamp`: to get a `date_string`
    - `date_string`: to get a `timestamp`

    Returns:
        JSON object with the converted value.
    """
    try:
        if data.timestamp is not None:
            # Convert UNIX timestamp to ISO-formatted UTC string
            dt = datetime.utcfromtimestamp(data.timestamp)
            return {"date_string": dt.isoformat()}

        elif data.date_string is not None:
            # Convert ISO date string to UNIX timestamp (assumed UTC)
            dt = datetime.fromisoformat(data.date_string).replace(tzinfo=timezone.utc)
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
