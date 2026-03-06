from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

router = Router()


class ProfileState(StatesGroup):
    editing = State()


def profile_navigation():
    builder = InlineKeyboardBuilder()
    builder.button(text="🔙 Главное меню", callback_data="main_menu")
    return builder.as_markup()


@router.callback_query(F.data == "profile")
async def profile_callback(callback: CallbackQuery, state: FSMContext):
    if isinstance(callback.message, Message):
        await callback.message.edit_text(
            "Привет из профиля", reply_markup=profile_navigation()
        )
    await callback.answer()
