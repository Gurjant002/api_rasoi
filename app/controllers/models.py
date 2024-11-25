from pydantic import BaseModel


class Client(BaseModel):
  name: str
  srnames: str
  company: str
  nif: str
  address: str
  city: str
  postcode: int
  phone: int
  email: str