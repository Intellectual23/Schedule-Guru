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
        "schedule_id INTEGER,"
        "title TEXT, "
        "st_date TEXT, "
        "end_date TEXT)"
    )
    c.execute(
        "CREATE TABLE IF NOT EXISTS schedules ("
        "id INTEGER PRIMARY KEY AUTOINCREMENT,"
        "schedule_name TEXT,"
        "user_id INTEGER,"
        "group_url TEXT)"
    )
    db.commit()


async def add_user(user_id, username):
    user = c.execute("SELECT * FROM users WHERE tg_id == {key}".format(key=user_id)).fetchone()
    if not user:
        c.execute("INSERT INTO users (tg_id, username) VALUES (?,?)", (user_id, username))
        db.commit()


async def add_event(schedule_id, title, st_date, end_date):
    c.execute("INSERT INTO events (schedule_id, title, st_date, end_date) VALUES (?,?,?,?)",
              (schedule_id, title, st_date, end_date))
    db.commit()


async def add_schedule(schedule_name, admin_id, group_url):
    c.execute("INSERT INTO schedules (schedule_name, user_id, group_url) VALUES (?,?,?)",
              (schedule_name, admin_id, group_url))
    db.commit()


async def get_schedule_id(group_url):
    schedule = c.execute("SELECT id FROM schedules WHERE group_url = ?", (group_url,)).fetchone()
    if schedule:
        return schedule[0]
    return None
