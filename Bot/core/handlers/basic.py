from aiogram import Bot
from aiogram.types import Message
from core.utils.parser import read_data

async def get_start(message: Message, bot: Bot):
    await message.answer(f'Привет, {message.from_user.first_name}!')


async def get_data(message: Message, bot: Bot):
    await message.answer(f'Файл получен')
    file = await bot.get_file(message.document.file_id)
    await bot.download_file(file.file_path, 'data.xlsx')
    await read_data('data.xlsx')


async def get_help(message: Message, bot: Bot):
    await message.answer(f'- Отправьте расписание Вашего мероприятия в формате xlsx\n- Добавьте меня в группу мероприятия')

