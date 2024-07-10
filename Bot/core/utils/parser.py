import csv
import aiofiles
import core.data.database as db


async def read_data(file_name, schedule_id):
    async with aiofiles.open(file_name, mode='r', encoding='utf-8') as f:
        contents = await f.read()
        rows = csv.reader(contents.splitlines(), delimiter=';')
        for row in rows:
            title = row[0]
            st_date = row[1]
            end_date = row[2]
            print(schedule_id, title, st_date, end_date)
            await db.add_event(schedule_id, title, st_date, end_date)
