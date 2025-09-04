import logging
import sys
import asyncio

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from config import BotSettings

dp = Dispatcher()
bot = Bot(
    token=BotSettings.token, default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)


async def main() -> None:
    logging.info("Bot started")
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
