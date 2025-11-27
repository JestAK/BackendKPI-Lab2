import uuid
from record import delete_records_by_category

categories = {}

def gen_category_id():
    category_id = uuid.uuid4().hex
    return category_id


def create_category(name: str) -> dict:
    category_id = gen_category_id()
    category = {"id": category_id, "name": name}
    categories[category_id] = category
    return category


def get_categories() -> list[dict]:
    return list(categories.values())


def delete_category(name: str) -> bool:
    ids_to_delete = [category_id for category_id, category in categories.items() if category["name"] == name]

    if not ids_to_delete:
        return False

    for category_id in ids_to_delete:
        delete_records_by_category(category_id)
        del categories[category_id]

    return True