import sqlite3 as sq

db = sq.connect('database.db')

c = db.cursor()


async def db_start():
    c.execute(
        "CREATE TABLE IF NOT EXISTS users ("
        "id INTEGER PRIMARY KEY AUTOINCREMENT, "
        "tg_id INTEGER,"
        "username TEXT, "
        "tg_group_id INTEGER,"
        "schedule_id TEXT)"
    )
    c.execute(
        "CREATE TABLE IF NOT EXISTS events ("
        "ev_id INTEGER PRIMARY KEY AUTOINCREMENT, "
        "tg_group_id INTEGER, "
        "title TEXT, "
        "st_date TEXT, "
        "end_date TEXT)"
    )
    db.commit()


async def add_user(user_id, username):
    user = c.execute("SELECT * FROM users WHERE tg_id == {key}".format(key=user_id)).fetchone()
    if not user:
        c.execute("INSERT INTO users (tg_id, username) VALUES (?,?)", (user_id, username))
        db.commit()


async def set_tg_group_id(user_id, group_id):
    user = c.execute("SELECT * FROM users WHERE tg_id = ?", (user_id,)).fetchone()
    if user:
        c.execute("UPDATE users SET tg_group_id = ? WHERE tg_id = ?", (group_id, user_id))
        db.commit()
    else:
        print(f"User with tg_id {user_id} not found.")
