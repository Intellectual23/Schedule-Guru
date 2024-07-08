import csv
import aiofiles
from core.schedule_data import Schedule, Event


async def read_data(file_name):
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
    await print_data(schedule)


async def print_data(schedule):
    for event in schedule.events:
        print(event.title, event.st_date, event.end_date)
