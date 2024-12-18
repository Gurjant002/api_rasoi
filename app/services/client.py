from sqlalchemy import select
from app.config.database.session import engine
from sqlmodel import Session
from app.models.client_model import Clients

def query_all_clients() -> list[dict]:
    with Session(engine) as session:
        clients = session.exec(select(Clients)).all()
        return clients

def add_client(client):
    clients = Clients.from_orm(client)
    with Session(engine) as session:
        session.add(clients)
        session.commit()