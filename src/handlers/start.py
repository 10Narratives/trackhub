from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart
from aiogram.utils.keyboard import InlineKeyboardBuilder

router = Router()


def start_navigation():
    builder = InlineKeyboardBuilder()
    builder.button(text="Профиль", callback_data="profile")
    return builder.as_markup()


@router.message(CommandStart)
async def start_command(message: Message):
    await message.answer("Добро пожаловать!", reply_markup=start_navigation())


@router.callback_query(F.data == "main_menu")
async def start_callback(callback: CallbackQuery):
    if isinstance(callback.message, Message):
        await callback.message.edit_text(
            "Добро пожаловать!", reply_markup=start_navigation()
        )
    await callback.answer()
