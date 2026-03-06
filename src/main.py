import asyncio

import structlog

from aiogram import Bot, Dispatcher

from config import TG_BOT_TOKEN, TRACE_FORMAT, TRACE_LEVEL
from handlers import register_routers
from utils.logging import setup_logger


async def main():
    setup_logger(trace_level=TRACE_LEVEL, trace_format=TRACE_FORMAT)

    logger = structlog.get_logger()
    logger.info(
        "starting application", trace_level=TRACE_LEVEL, trace_format=TRACE_FORMAT
    )

    bot = Bot(token=TG_BOT_TOKEN)

    dp = Dispatcher()
    register_routers(dp)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
