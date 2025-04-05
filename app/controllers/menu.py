from app.services.menu import (
    query_all_menu,
    insert_list_menu
)
from app.utils.menu_parser import menu_parser


def get_menus() -> dict:
    try:
        return query_all_menu()
    except Exception as e:
        raise e

def insert_menu(menu: dict) -> dict:
    try:
        menu_to_insert = query_all_menu()
        result = insert_list_menu(menu_to_insert)
        
    except Exception as e:
        raise e