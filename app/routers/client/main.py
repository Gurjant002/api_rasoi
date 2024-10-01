from fastapi import APIRouter
from app.controllers.client import get_clients

router = APIRouter()

@router.get("/get-client", tags=["client"])
async def get_client():
  try:
    return get_clients()
  except Exception as e:
    return {"error": str(e)}
