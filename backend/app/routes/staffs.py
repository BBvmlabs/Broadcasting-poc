from fastapi import APIRouter
from ..api.staff import staff_creation

router = APIRouter()

router.include_router(staff_creation.router)
# router.include_router(signup.router)