from fastapi import APIRouter
from app.controllers.menu import get_menus, insert_menu

router = APIRouter()

@router.get("/get-menu", tags=["Menu"])
async def get_menu():
  try:
    return get_menus()
  except Exception as e:
    return {"error": str(e)}

@router.post("/insert", tags=["Menu"])
async def add_menu():
  try:
    return 
  except Exception as e:
    return {"error": str(e)}