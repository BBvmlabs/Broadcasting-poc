from fastapi import APIRouter
from ..api.auth import login, signup

router = APIRouter()

router.include_router(login.router)
router.include_router(signup.router)