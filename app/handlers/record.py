import uuid
from datetime import datetime

records = {}

def gen_record_id():
    record_id = uuid.uuid4().hex
    return record_id


def create_record(user_id: str, category_id: str, cost: int) -> dict:
    record_id = gen_record_id()
    record = {
        "id": record_id,
        "user_id": user_id,
        "category_id": category_id,
        "datetime": datetime.now(),
        "cost": cost
    }
    records[record_id] = record
    return record

def get_record(record_id: int) -> dict | None:
    return records.get(record_id)

def get_records(user_id: str | None = None, category_id: str | None = None) -> list[dict]:
    result = list(records.values())

    if user_id is not None:
        result = [r for r in result if r["user_id"] == user_id]

    if category_id is not None:
        result = [r for r in result if r["category_id"] == category_id]

    return result


def delete_record(record_id: str) -> bool:
    if record_id not in records:
        return False
    del records[record_id]
    return True

def delete_records_by_user(user_id: str) -> bool:
    ids = [record_id for record_id, r in records.items() if r["user_id"] == user_id]
    for rid in ids:
        del records[rid]
    return True

def delete_records_by_category(category_id: str) -> bool:
    ids = [record_id for record_id, r in records.items() if r["category_id"] == category_id]
    for rid in ids:
        del records[rid]
    return True
