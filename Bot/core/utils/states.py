from aiogram.fsm.state import StatesGroup, State


class EventData(StatesGroup):
    name = State()
    group_nick = State()

