from aiogram import Bot, Router, F
from aiogram.client import bot
from aiogram.types import Message, ChatMember, ChatMemberUpdated
from aiogram.filters import CommandStart, Command, ChatMemberUpdatedFilter, JOIN_TRANSITION
from aiogram.enums import chat_type
from core.settings import settings
from core.data import database as db

router = Router()


@router.my_chat_member(ChatMemberUpdatedFilter(member_status_changed=JOIN_TRANSITION))
async def bot_added(event: ChatMemberUpdated):
    await db.set_tg_group_id(event.from_user.id, event.chat.id)
    print(event.from_user.id, event.chat.id)
    await event.answer(f'Всем привет, я буду обновлять информацию по расписанию мероприятия "{event.chat.title}"')
