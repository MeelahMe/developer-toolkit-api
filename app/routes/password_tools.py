from fastapi import APIRouter, Query, HTTPException
from pydantic import BaseModel, Field
import random
import string

# Create a router for password-related endpoints
router = APIRouter(prefix="/tools/password", tags=["Password Tools"])

# Response model for generated password
class PasswordResponse(BaseModel):
    password: str = Field(
        example="a9B!7xTq@1l#",
        description="A randomly generated secure password"
    )

@router.get(
    "/generate",
    response_model=PasswordResponse,
    summary="Generate a secure random password",
    response_description="Returns a randomly generated password based on provided criteria"
)
def generate_password(
    length: int = Query(12, ge=4, le=128, description="Length of the password (4–128)"),
    include_symbols: bool = Query(True, description="Include special characters (!@#...)"),
    include_numbers: bool = Query(True, description="Include digits (0-9)"),
    include_uppercase: bool = Query(True, description="Include uppercase letters (A-Z)"),
    include_lowercase: bool = Query(True, description="Include lowercase letters (a-z)")
):
    """
    Generate a secure password with customizable parameters.

    Parameters:
        - length: total number of characters in the password
        - include_symbols: include special characters like !@#$%
        - include_numbers: include digits 0–9
        - include_uppercase: include uppercase letters A–Z
        - include_lowercase: include lowercase letters a–z

    Returns:
        PasswordResponse: A JSON object containing the generated password.
    """
    character_pool = ""

    # Build character pool based on options
    if include_lowercase:
        character_pool += string.ascii_lowercase
    if include_uppercase:
        character_pool += string.ascii_uppercase
    if include_numbers:
        character_pool += string.digits
    if include_symbols:
        character_pool += string.punctuation

    # Ensure there's at least one character type selected
    if not character_pool:
        raise HTTPException(
            status_code=400,
            detail="At least one character set must be selected."
        )

    # Generate password using random choices from pool
    password = ''.join(random.choices(character_pool, k=length))
    return {"password": password}

