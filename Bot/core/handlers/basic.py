from aiogram import Bot, Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from core.utils.parser import read_data
from core.data import database as db

router = Router()
router.message.filter(F.chat.type != 'supergroup')


@router.message(CommandStart())
async def get_start(message: Message):
    await db.add_user(message.from_user.id, message.from_user.username)
    await message.answer(f'Привет, {message.from_user.first_name}!')


@router.message(F.document)
async def get_data(message: Message, bot: Bot):
    file = await bot.get_file(message.document.file_id)
    await bot.download_file(file.file_path, 'data.csv')
    await read_data('data.csv')
    await message.answer(f'Файл получен')


@router.message(Command(commands=['help']))
async def get_help(message: Message):
    await message.answer(
        f'- Отправьте расписание Вашего мероприятия в формате csv\n- Добавьте меня в группу мероприятия')
