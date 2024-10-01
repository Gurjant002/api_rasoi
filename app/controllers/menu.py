from app.services.menu import (
    query_all_menu,
)
from app.utils.menu_parser import menu_parser


def get_menus() -> dict:
    try:
        return query_all_menu()
    except Exception as e:
        raise e
