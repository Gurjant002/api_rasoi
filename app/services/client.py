from sqlalchemy import select
from app.config.database.session import get_session, engine
from sqlmodel import Session
from app.models.client_model import Clients

def query_all_clients() -> list:
    """
    Queries all clients from the database.

    Returns:
        sqlalchemy.engine.result.Result: All clients from the database.
    """
    results = get_session().exec(select(Clients)).all()

    return results

def add_client(client):
    clients = Clients.from_orm(client)
    with Session(engine) as session:
        session.add(clients)
        session.commit()