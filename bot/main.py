import logging
import sys
import asyncio

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage

from config import BotSettings
from views import router

dp = Dispatcher(storage=MemoryStorage())
bot = Bot(
    token=BotSettings.token, default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)


async def main() -> None:
    logging.info("Bot started")
    dp.include_router(router)
    await dp.start_polling(bot)



if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
