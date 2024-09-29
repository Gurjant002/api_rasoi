from fastapi import APIRouter

from app.routers.menu.main import router as menu_item_router

router = APIRouter()
router.include_router(menu_item_router, prefix="/menu")