#USERS
#QUESTIONS
#RESULTS

CREATE_USERS_TABLE = '''
    CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    telegram_id INTEGER NOT NULL UNIQUE,
    username TEXT
    )
'''

CREATE_QUESTIONS_TABLE = '''
    CREATE TABLE IF NOT EXISTS questions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question_text TEXT NOT NULL,
    correct_answer TEXT NOT NULL
    )
    '''

CREATE_RESULTS_TABLE = '''
    CREATE TABLE IF NOT EXISTS results (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    users_id INTEGER NOT NULL,
    question_id INTEGER NOT NULL,
    is_correct BOOLEAN NOT NULL DEFAULT 0,
    FOREIGN KEY (users_id) REFERENCES users (id) ON DELETE CASCADE,
    FOREIGN KEY (question_id) REFERENCES questions (id) ON DELETE CASCADE
    )
    '''


    # CRUD- Create, Read, Update, Delete

    # --USERS--
GET_USER_BY_TG_ID = 'SELECT * FROM users WHERE telegram_id = ?'

INSERT_USER = 'INSERT OR IGNORE INTO users (telegram_id, username) VALUES (?, ?)'

UPDATE_USER_USERNAME = 'UPDATE users SET username = ? WHERE telegram_id = ?'

DELETE_USER = 'DELETE FROM users WHERE telegram_id = ?'



GET_ALL_QUESTIONS = 'SELECT * FROM questions'

GET_QUESTION_BY_ID = 'SELECT * FROM questions WHERE id = ?'

INSERT_QUESTION = 'INSERT INTO questions (question_text, correct_answer) VALUES (?, ?)'

INSWERT_RESULT = 'INSERT INTO results (users_id, question_id, is_correct) VALUES (?, ?, ?)'

GET_SCORE_BY_USER_ID = 'SELECT COUNT(*) AS total, SUM(is_correct) AS score FROM results WHERE users_id = ?'


UPDATE_QUESTION_TEXT = 'UPDATE questions SET question_text = ? WHERE id = ?'

DELETE_QUESTION = 'DELETE FROM questions WHERE id = ?'

UPDATE_RESULT = 'UPDATE results SET is_correct = ? WHERE id = ?'

DELETE_RESULTS_BY_USER = 'DELETE FROM results WHERE users_id = ?'

GET_USER_ANSWERS = '''
SELECT users.username, questions.question_text, results.is_correct
FROM results
INNER JOIN users ON users.id = results.users_id
INNER JOIN questions ON questions.id = results.question_id
WHERE users.telegram_id = ?
'''