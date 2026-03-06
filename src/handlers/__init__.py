from aiogram import Dispatcher

from .start import router as start_router

def register_routers(dp: Dispatcher):
  dp.include_routers(start_router)