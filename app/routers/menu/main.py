from fastapi import APIRouter
from app.controllers.menu import get_menus

router = APIRouter()

@router.get("/get-menu", tags=["Menu"])
async def get_menu():
  try:
    return get_menus()
  except Exception as e:
    return {"error": str(e)}

@router.post("/add-plate", tags=["Menu"])
async def add_plate():
  return {"menu": "Khush"}

@router.put("/update-plate", tags=["Menu"])
async def update_plate():
  return {"menu": "Khush"}

@router.delete("/delete-plate", tags=["Menu"])
async def delete_plate():
  return {"menu": "Khush"}

