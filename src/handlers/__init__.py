from aiogram import Dispatcher

from .start import router as start_router
from .profile import router as profile_router


def register_routers(dp: Dispatcher):
    dp.include_routers(start_router, profile_router)
