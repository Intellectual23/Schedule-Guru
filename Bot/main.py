from aiogram import Bot, Dispatcher
import asyncio
import logging
from core.settings import settings
from core.handlers.basic import router as basic_router
from core.handlers.group import router as group_router
from core.utils.commands import set_commands
from core.data import database as db
from aiogram.enums import ParseMode
from core.schedule_data import Event, Schedule

token = settings.bots.bot_token
admin_id = settings.bots.admin_id


async def on_startup(bot: Bot):
    await set_commands(bot)
    await db.db_start()
    print('- bot started')


async def main():
    bot = Bot(token=token)
    dp = Dispatcher()
    dp.include_routers(
        basic_router,
        group_router
    )
    dp.startup.register(on_startup)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Bot disabled.')
