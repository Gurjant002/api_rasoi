import json

def read_json():
  with open("data/restaurant_menu.json") as f:
    return json.load(f)

def query_all_menu() -> list[dict]:
  menu = read_json()
  return menu
