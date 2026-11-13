from db.database import get_db
from db.qyeries import INSWERT_RESULT, GET_SCORE_BY_USER_ID, UPDATE_RESULT, DELETE_RESULTS_BY_USER, GET_USER_ANSWERS

def save_result(users_id: int, question_id: int, is_correct: bool):
    conn = get_db()
    conn.execute(INSWERT_RESULT, (users_id, question_id, int(is_correct)))
    conn.commit()
    conn.close()

def get_score(users_id: int):
    conn = get_db()
    row = conn.execute(GET_SCORE_BY_USER_ID, (users_id,)).fetchone()
    conn.close()
    return dict(row) if row else {'total': 0, 'score': 0}

def update_result(result_id: int, is_correct: bool):
    conn = get_db()
    conn.execute(UPDATE_RESULT, (int(is_correct), result_id))
    conn.commit()
    conn.close()


def delete_results_by_user(users_id: int):
    conn = get_db()
    conn.execute(DELETE_RESULTS_BY_USER, (users_id,))
    conn.commit()
    conn.close()

def get_user_answers(telegram_id: int):
    conn = get_db()
    rows = conn.execute(GET_USER_ANSWERS, (telegram_id,)).fetchall()
    conn.close()
    return [dict(row) for row in rows]