import json
from app.models.menu_model import Plate

def read_json():
  with open("data/restaurant_menu.json") as f:
    return json.load(f)

def query_all_menu() -> list[dict]:
  menu = read_json()
  return menu

def insert_list_menu(menu: list[dict]) -> list[dict]:
  print(menu)
  return menu
