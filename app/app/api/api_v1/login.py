import os
from fastapi import APIRouter,HTTPException
from typing import *
router = APIRouter()


@router.post("/login/access-token", response_model=Any)
def login_access_token(
    
) -> Any:
    """
    OAuth2 compatible token login, get an access token for future requests
    """
    return {
        "access_token": os.getenv('POSTGRES_SERVER'),
        "token_type": "bearer",
    }

