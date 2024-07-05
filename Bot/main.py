from aiogram import Bot, Dispatcher
from aiogram.types import Message
import asyncio

from core.handlers.basic import get_start
from core.settings import settings

token = settings.bots.bot_token
admin_id = settings.bots.admin_id


async def start_bot(bot: Bot):
    await bot.send_message(admin_id, text='BOT STARTED')


async def stop_bot(bot: Bot):
    await bot.send_message(admin_id, text='BOT STOPPED')





async def main():
    bot = Bot(token=token)
    dp = Dispatcher()
    
    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)
    dp.message.register(get_start, bot)


    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Bot disabled.')
