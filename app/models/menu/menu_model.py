from typing import Dict, List
from pydantic import BaseModel

class Plate(BaseModel):
  """A plate in the menu
  
  Attributes:
      name (str): Name of the plate
      description (str): Description of the plate
      price (float): Price of the plate
  """
  name: str
  description: str
  price: float
