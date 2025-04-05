from pydantic import BaseModel
from decimal import Decimal
from sqlmodel import Field, Relationship, SQLModel

class Menu(SQLModel, table=True):
  id: int = Field(default=None, primary_key=True)
  name: str = Field(max_length=45, nullable=False)
  description: str = Field(max_length=50, nullable=False)
  price: Decimal = Field(max_digits=10, decimal_places=2, nullable=False)
  id_cat: int = Field(max_length=9, nullable=False, foreign_key="category.id")
  active: bool = Field(default=True, nullable=False)

class menu(BaseModel):
    """
    A plate in the menu

    Attributes:
        name (str): Name of the plate
        description (str): Description of the plate
        price (float): Price of the plate
    """

    name: str
    description: str
    price: float
