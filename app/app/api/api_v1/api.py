from fastapi import APIRouter

from app.api.api_v1 import login

api_router = APIRouter()
api_router.include_router(login.router, tags=["login"])
# api_router.include_router(domain.router, prefix="/domain", tags=["domain"]) 
# api_router.include_router(department.router, prefix="/department", tags=["department"])
# api_router.include_router(module.router, prefix="/module", tags=["module"])
# api_router.include_router(uac.router, prefix="/uac", tags=["uac"])
# api_router.include_router(users.router, prefix="/users", tags=["users"])