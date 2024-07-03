from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import Command, CommandStart

import asyncio

bot = Bot(token='7448681372:AAHFmbKEouZb6uihY50EWQr-38AR3zgtxtI')
dp = Dispatcher()


@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Привет!')


@dp.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer('Руководство: ')


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Bot disabled.')
