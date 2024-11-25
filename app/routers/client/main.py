from fastapi import APIRouter
from app.controllers.client import get_clients, create_client
from app.controllers.models import Client

router = APIRouter()

@router.get("/get-client", tags=["client"])
async def get_client():
  try:
    return get_clients()
  except Exception as e:
    return {"error": str(e)}

@router.post("/add-client", tags=["client"])
async def add_client(client: Client):
  try:
    return create_client(client)
  except Exception as e:
    return {"error": str(e)}
  
