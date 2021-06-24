from typing import List

from asgiref.sync import sync_to_async
from admin_panel.usersmanage.models import Item, User


@sync_to_async
def get_categories() -> List:
    pass


@sync_to_async
def get_subcategories() -> List:
    pass


@sync_to_async
def count_items():
    pass


@sync_to_async
def get_items() -> List:
    pass


@sync_to_async
def get_item() -> List:
    pass
