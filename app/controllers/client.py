from app.models.client_model import Clients
from app.services.client import (
  query_all_clients, 
  add_client
)
# from app..client_parser import client_parser

def get_clients() -> dict:
  try:
    return query_all_clients()
  except Exception as e:
    raise e

def create_client(client: Clients):
  try:
    return add_client(client)
  except Exception as e:
    raise e
