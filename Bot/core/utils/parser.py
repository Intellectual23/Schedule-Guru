import csv
import aiofiles
from core.schedule_data import Schedule, Event
import core.data.database as db


async def read_data(file_name, name, tg_group_nick):
    schedule = Schedule(name='Мероприятие')
    async with aiofiles.open(file_name, mode='r', encoding='utf-8') as f:
        contents = await f.read()
        rows = csv.reader(contents.splitlines(), delimiter=';')
        for row in rows:
            title = row[0]
            st_date = row[1]
            end_date = row[2]
            cur_event = Event(title=title, st_date=st_date, end_date=end_date)
            schedule.events.append(cur_event)
            print(name, tg_group_nick, cur_event.title, st_date, end_date)
            await db.add_event(f'{name}', f'{tg_group_nick}', title, st_date, end_date)
