from app.models.client_model import Clients
from app.controllers.models import Client
from app.services.client import (
    query_all_clients, 
    add_client
)
# from app..client_parser import client_parser

def get_clients():
    try:
        client_list: list[Client] = []
        query = query_all_clients()
        
        for client in query:
            client_list.append(client.Clients)
            
        return client_list
    except Exception as e:
        raise e

def create_client(client: Clients):
    try:
        return add_client(client)
    except Exception as e:
        raise e
