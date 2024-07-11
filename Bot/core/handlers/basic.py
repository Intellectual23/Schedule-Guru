from aiogram import Bot, Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
from core.utils.parser import read_data
from core.data import database as db
from core.utils.states import EventData

router = Router()
router.message.filter(F.chat.type != 'supergroup')


@router.message(CommandStart())
async def get_start(message: Message):
    await db.add_user(message.from_user.id, message.from_user.username)
    await message.answer(f'Здравствуйте, {message.from_user.first_name}!\n'
                         f'Отправьте расписание Вашего мероприятия в формате `.csv`.\n'
                         f'Подробнее о формате расписания можете прочесть в /help.')


@router.message(F.document)
async def get_data(message: Message, bot: Bot, state: FSMContext):
    file = await bot.get_file(message.document.file_id)
    await bot.download_file(file.file_path, 'data.csv')
    await message.answer("Введите название мероприятия:")
    await state.set_state(EventData.name)


@router.message(EventData.name)
async def get_name(message: Message, state: FSMContext):
    event_name = message.text
    await state.update_data(name=event_name)
    await message.answer("Хорошо, теперь отправьте url Вашего группового чата мероприятия:")
    await state.set_state(EventData.group_nick)


@router.message(EventData.group_nick)
async def set_nick(message: Message, state: FSMContext):
    event_group_nick = message.text
    await state.update_data(group_id=event_group_nick)
    data = await state.get_data()
    await db.add_schedule(data['name'], message.from_user.id, event_group_nick)
    schedule_id = await db.get_schedule_id(event_group_nick)
    await read_data('data.csv', schedule_id)
    await message.answer(
        f"Файл получен, название мероприятия: {data['name']}\nМожете добавить меня в {event_group_nick}.")
    await state.clear()


@router.message(Command(commands=['help']))
async def get_help(message: Message):
    await message.answer(
        f'Инструкция:\n-\tОтправьте расписание Вашего мероприятия в формате csv. '
        f'Данные должны быть представлены в трех столбцах: <название события>;'
        f'<время начала события>(timestamp);<время конца события(timestamp)>'
        f'\n-\tВведите название мероприятия.'
        f'\n-\tВведите url группового чата мероприятия.'
        f'\n-\tДобавьте меня в групповой чат мероприятия.')
