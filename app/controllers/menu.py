from app.services.menu import (
  query_all_menu,
)
from app.utils.menu_parser import menu_parser
def get_menus() -> dict:
  try:
    menu = query_all_menu()
    return menu_parser(menu)
  except Exception as e:
    raise e
