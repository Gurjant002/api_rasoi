from fastapi import APIRouter

from app.routers.menu.main import router as menu_item_router
from app.routers.client.main import router as client_router

router = APIRouter()
router.include_router(menu_item_router, prefix="/menu", tags=["Menu"])
router.include_router(client_router, prefix="/client", tags=["Clients"])