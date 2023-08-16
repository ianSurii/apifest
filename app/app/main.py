import os
from typing import Any
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse

# from app.api.api_v1.api import api_router
# from app.core.config import settings

app = FastAPI(
#     title=settings.PROJECT_NAME, openapi_url=f"{settings.API_V1_STR}/openapi.json"
)
    

# # Set all CORS enabled origins
# if settings.BACKEND_CORS_ORIGINS:
#     app.add_middleware(
#         CORSMiddleware,
#         allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
#         allow_credentials=True,
#        allow_methods=["*"],
#         allow_headers=["*"],
#     )

# app.include_router(api_router, prefix=settings.API_V1_STR)
@app.get("/")
def read_root():   
   
    return  RedirectResponse(url="/docs/")

@app.get("/registeruser",response_model=Any)
def register_user(
    
) -> Any:
    """
    Register User
    """
    return {
       
    }

@app.get("",response_model=Any)
def get_access_token(
    
) -> Any:
    """
    OAuth2 compatible token login, get an access token for future requests
    """
    return {
        "access_token": os.getenv('POSTGRES_SERVER'),
        "token_type": "bearer",
    }

@app.get("request",response_model=Any)
def reques_services(
    
) -> Any:
    """
    OAuth2 compatible token login, get an access token for future requests
    """
    return {
        "access_token": os.getenv('POSTGRES_SERVER'),
        "token_type": "bearer",
    }
   
   


