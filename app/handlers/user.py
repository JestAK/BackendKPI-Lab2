users = {}

user_counter = 0

def gen_user_id():
    global user_counter
    user_id = user_counter
    user_counter += 1
    return user_id

def create_user(name: str) -> dict:
    user_id = gen_user_id()
    user = {"id": user_id, "name": name}
    users[user_id] = user
    return user

def get_user(user_id: int) -> dict | None:
    return users.get(user_id)


def delete_user(user_id: int) -> bool:
    if user_id not in users:
        return False

    del users[user_id]

    return True


def list_users() -> list[dict]:
    return list(users.values())