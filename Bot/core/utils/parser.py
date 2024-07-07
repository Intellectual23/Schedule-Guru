import openpyxl
from core.schedule_data import Schedule, Event
import datetime


async def read_data(file_name):
    book = openpyxl.open(file_name, read_only=True)
    sheet = book.active
    schedule = Schedule(name='Мероприятие')
    schedule.name = 'Мероприятие'
    for row in range(1, sheet.max_row + 1):
        name = sheet[row][0].value
        time_str = sheet[row][1].value.strftime('%H:%M')
        time = datetime.datetime.strptime(time_str, '%H:%M').time()
        description = sheet[row][2].value
        cur_event = Event(name=name, time=time, description=description)
        schedule.events.append(cur_event)
    await print_data(schedule)


async def print_data(schedule):
    for event in schedule.events:
        print(event.name, event.time, event.description)
