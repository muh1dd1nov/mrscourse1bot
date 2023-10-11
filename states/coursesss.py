from aiogram.dispatcher.filters.state import StatesGroup, State

class CoursesState(StatesGroup):
    courses = State()
    items = State()
    clients = State()