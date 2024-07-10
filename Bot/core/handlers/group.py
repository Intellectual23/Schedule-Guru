from sched import scheduler

from aiogram import Bot, Router, F
from aiogram.client import bot
from aiogram.types import Message, ChatMember, ChatMemberUpdated
from aiogram.filters import CommandStart, Command, ChatMemberUpdatedFilter, JOIN_TRANSITION
from aiogram.enums import chat_type
from core.settings import settings
from core.data import database as db
from core.schedule_data import Event
import asyncio, datetime

router = Router()


@router.my_chat_member(ChatMemberUpdatedFilter(member_status_changed=JOIN_TRANSITION))
async def bot_added(event: ChatMemberUpdated):
    print(event.from_user.id, event.chat.id, event.chat.username)

    chat_url = f'https://t.me/{event.chat.username}'
    id = await db.get_schedule_id(chat_url)
    schedule = await db.get_schedule(id)
    name = await db.get_schedule_name(id)

    await event.answer(f'Всем привет, я буду обновлять информацию по расписанию мероприятия "{name}"')

    ev_list = []
    cur_events = []

    for ev in schedule:
        new_ev = Event(ev[2], ev[3], ev[4])
        ev_list.append(new_ev)

    ##sort ev_list
    while len(ev_list) > 0:
        is_updated = False
        while int(ev_list[0].st_date) <= int(datetime.datetime.now().timestamp()):
            cur_events.append(ev_list.pop(0))
            is_updated = True
        for ev in cur_events:
            if int(ev.end_date) < int(datetime.datetime.now().timestamp()):
                cur_events.remove(ev)
                is_updated = True
        if is_updated:
            msg = 'Current Events:\n'
            for ev in cur_events:
                msg += (f'{ev.title}: {datetime.datetime.fromtimestamp(ev.st_date)} - '
                        f'{datetime.datetime.fromtimestamp(ev.end_date)}\n')
            await event.answer(msg)

