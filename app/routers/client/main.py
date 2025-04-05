from fastapi import APIRouter
from app.controllers.client import get_clients, create_client
from app.controllers.models import Client

router = APIRouter()

@router.get("/get-client", tags=["Client"], response_model=list[Client])
async def get_client():
  try:
    response = get_clients()
    return response
  except Exception as e:
    return {"error": str(e)}

@router.post("/add-client", tags=["Client"])
async def add_client(client: Client):
  try:
    return create_client(client)
  except Exception as e:
    return {"error": str(e)}
  
