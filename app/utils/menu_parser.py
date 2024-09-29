from app.models.menu.menu_model import (
  Plate,
)


def plate_parser(plate: dict) -> Plate:
  """
  This function parses a dictionary representing a plate and returns a Plate object.
  
  Args:
    plate (dict): A dictionary containing the plate's attributes.
  
  Returns:
    Plate: A Plate object created from the input dictionary.
  """
  return Plate(
    name=plate["Name"],
    description=plate["Description"],
    price=plate["Price"],
  )

def menu_parser(menu: dict) -> dict:
  """
  This function parses a list of dictionaries representing menu items and returns a Menu object.
  
  Args:
    menu (list[dict]): A list of dictionaries containing the menu items' attributes.
  
  Returns:
    Menu: A Menu object created from the input list of dictionaries.
  """
  categories = list(menu.keys())
  dict_plates = menu[list(menu.keys())[0]]
  list_of_categories = menu[list(menu.keys())[0]].keys()

  category_dict = {}
  
  
  for category in list_of_categories:
    for plate in dict_plates[category]:
      parsed_plate = plate_parser(plate)

  return menu