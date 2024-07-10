from aiogram import Bot, Router, F
from aiogram.client import bot
from aiogram.types import Message, ChatMember, ChatMemberUpdated
from aiogram.filters import CommandStart, Command, ChatMemberUpdatedFilter, JOIN_TRANSITION
from aiogram.enums import chat_type
from core.settings import settings
from core.data import database as db
import asyncio

router = Router()


@router.my_chat_member(ChatMemberUpdatedFilter(member_status_changed=JOIN_TRANSITION))
async def bot_added(event: ChatMemberUpdated):
    print(event.from_user.id, event.chat.id)
    # find with db event name by group id
    await event.answer(f'Всем привет, я буду обновлять информацию по расписанию мероприятия "{event.chat.title}"')

    async def send_greetings():
        while True:
            await event.answer(f'Всем привет из мероприятия "{event.chat.title}"!')
            await asyncio.sleep(5)

    await asyncio.create_task(send_greetings())
