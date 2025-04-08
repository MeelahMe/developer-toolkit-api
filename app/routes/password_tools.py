from fastapi import APIRouter, Query, HTTPException
from pydantic import BaseModel, Field
import random
import string

router = APIRouter(prefix="/tools/password", tags=["Password Tools"])

# Response model for password generation
class PasswordResponse(BaseModel):
    password: str = Field(
        example="a9B!7xTq@1l#",
        description="A randomly generated password"
    )

@router.get(
    "/generate",
    response_model=PasswordResponse,
    summary="Generate a secure random password",
    response_description="Returns a randomly generated password based on query parameters"
)
def generate_password(
    length: int = Query(12, ge=4, le=128, description="Length of the password"),
    include_symbols: bool = Query(True, description="Include special characters"),
    include_numbers: bool = Query(True, description="Include digits"),
    include_uppercase: bool = Query(True, description="Include uppercase letters"),
    include_lowercase: bool = Query(True, description="Include lowercase letters")
):
    """
    Generate a secure, random password.

    You can customize:
    - Length
    - Whether to include symbols, numbers, uppercase, and lowercase characters

    Returns:
        A JSON object containing the generated password.
    """
    character_pool = ""

    if include_lowercase:
        character_pool += string.ascii_lowercase
    if include_uppercase:
        character_pool += string.ascii_uppercase
    if include_numbers:
        character_pool += string.digits
    if include_symbols:
        character_pool += string.punctuation

    if not character_pool:
        raise HTTPException(
            status_code=400,
            detail="At least one character set must be selected."
        )

    password = ''.join(random.choices(character_pool, k=length))
    return {"password": password}

