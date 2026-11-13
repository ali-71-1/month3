from db.database import get_db
from db.qyeries import (
    GET_ALL_QUESTIONS,
    GET_QUESTION_BY_ID,
    INSERT_QUESTION,
    UPDATE_QUESTION_TEXT,
    DELETE_QUESTION,
)


def get_question(question_id: int):
    conn = get_db()
    question = conn.execute(GET_QUESTION_BY_ID, (question_id,)).fetchone()
    conn.close()
    return dict(question) if question else None


def create_question(question_text: str, correct_answer: str):
    conn = get_db()
    cursor = conn.execute(INSERT_QUESTION, (question_text, correct_answer))
    conn.commit()
    new_id = cursor.lastrowid
    conn.close()
    return get_question(new_id)


def update_question_text(question_id: int, new_text: str):
    conn = get_db()
    conn.execute(UPDATE_QUESTION_TEXT, (new_text, question_id))
    conn.commit()
    conn.close()
    return get_question(question_id)


def delete_question(question_id: int):
    conn = get_db()
    conn.execute(DELETE_QUESTION, (question_id,))
    conn.commit()
    conn.close()

def get_all_questions():
    conn = get_db()
    rows = conn.execute(GET_ALL_QUESTIONS).fetchall()
    conn.close()
    return [dict(row) for row in rows]