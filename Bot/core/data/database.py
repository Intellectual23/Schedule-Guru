import sqlite3 as sq

db = sq.connect('database.db')

c = db.cursor()


async def db_start():
    c.execute(
        "CREATE TABLE IF NOT EXISTS users ("
        "id INTEGER PRIMARY KEY AUTOINCREMENT, "
        "tg_id INTEGER,"
        "username TEXT)"
    )
    c.execute(
        "CREATE TABLE IF NOT EXISTS events ("
        "id INTEGER PRIMARY KEY AUTOINCREMENT,"
        "schedule_name TEXT,"
        "group_nick TEXT, "
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


async def add_event(schedule_name, group_nick, title, st_date, end_date):
    c.execute("INSERT INTO events (schedule_name, group_nick, title, st_date, end_date) VALUES (?,?,?,?,?)",
              (schedule_name, group_nick, title, st_date, end_date))
    db.commit()
