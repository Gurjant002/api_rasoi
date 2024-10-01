from app.services.client import (
    query_all_clients
)
# from app..client_parser import client_parser

def get_clients() -> dict:
    try:
        return query_all_clients()
    except Exception as e:
        raise e
