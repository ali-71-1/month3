from db.database import get_db
from db.qyeries import DELETE_USER, GET_USER_BY_TG_ID, INSERT_USER, UPDATE_USER_USERNAME

def get_user(telegram_id: int):
    conn = get_db()
    user = conn.execute(GET_USER_BY_TG_ID, (telegram_id,)).fetchone()
    conn.close()
    return dict(user) if user else None

def create_user(telegram_id: int, username: str):
    conn = get_db()
    conn.execute(INSERT_USER, (telegram_id, username))
    conn.commit()
    conn.close()
    return get_user(telegram_id)

def update_user_username(telegram_id: int, new_username: str):
    conn = get_db()
    conn.execute(UPDATE_USER_USERNAME, (new_username, telegram_id))
    conn.commit()
    conn.close()
    return get_user(telegram_id)

def delete_user(telegram_id: int):
    conn = get_db()
    conn.execute(DELETE_USER, (telegram_id,))
    conn.commit()
    conn.close()