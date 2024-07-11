import asyncio
from aiogram import Bot, Router
from aiogram.types import ChatMemberUpdated
from aiogram.filters import ChatMemberUpdatedFilter, JOIN_TRANSITION
from core.data import database as db
from core.schedule_data import Event
import datetime

router = Router()


@router.my_chat_member(ChatMemberUpdatedFilter(member_status_changed=JOIN_TRANSITION))
async def bot_added(event: ChatMemberUpdated, bot: Bot):
    print(
        f'- new schedule initialized: admin_id: {event.from_user.id}, '
        f'group_id: {event.chat.id}, '
        f'chat username: {event.chat.username}')

    chat_url = f'https://t.me/{event.chat.username}'
    sch_id = await db.get_schedule_id(chat_url)
    schedule = await db.get_schedule(sch_id)
    name = await db.get_schedule_name(sch_id)

    async def schedule_process():
        await event.answer(f'Всем привет, я буду обновлять информацию по расписанию мероприятия "{name}"')

        ev_list = []
        cur_events = []

        for ev in schedule:
            new_ev = Event(ev[2], ev[3], ev[4])
            ev_list.append(new_ev)

        ev_list.sort(key=lambda x: x.st_date)

        while ev_list or cur_events:
            is_updated = False
            current_time = int(datetime.datetime.now().timestamp())

            while ev_list and ev_list[0].st_date <= current_time:
                cur_events.append(ev_list.pop(0))
                is_updated = True

            if cur_events and is_updated:
                msg = 'Текущие события:\n'

                for ev in cur_events:
                    msg += (f'{ev.title}: {datetime.datetime.fromtimestamp(ev.st_date)} - '
                            f'{datetime.datetime.fromtimestamp(ev.end_date)}\n')
                if len(ev_list) > 0:
                    msg += (
                        f'Предстоящее событие:\n{ev_list[0].title}: {datetime.datetime.fromtimestamp(ev_list[0].st_date)} - '
                        f'{datetime.datetime.fromtimestamp(ev_list[0].end_date)}\n')
                await event.answer(msg)

            cur_events = [ev for ev in cur_events if ev.end_date > current_time]

            if not ev_list and not cur_events:
                await event.answer(f'Событий в расписании "{name}" больше нет!')

            await asyncio.sleep(60)

        await db.clear_schedule(sch_id)
        await bot.send_message(event.from_user.id, f'Мероприятие "{name}" подошло к концу!')

    await asyncio.create_task(schedule_process())
