from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, ContentType
import asyncio
import logging
from aiogram.filters import Command
from core.utils.commands import set_commands

from core.handlers.basic import get_start, get_data, get_help
from core.settings import settings

token = settings.bots.bot_token
admin_id = settings.bots.admin_id


async def start_bot(bot: Bot):
    await set_commands(bot)
    await bot.send_message(admin_id, text='BOT STARTED')


async def stop_bot(bot: Bot):
    await bot.send_message(admin_id, text='BOT STOPPED')


async def main():
    bot = Bot(token=token)
    dp = Dispatcher()

    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)
    dp.message.register(get_data, F.document)
    dp.message.register(get_start, Command(commands=['start']))
    dp.message.register(get_help, Command(commands=['help']))

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Bot disabled.')
