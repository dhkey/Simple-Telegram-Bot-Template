import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
            logging.StreamHandler()
        ]
)

import asyncio
import structlog
from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
import handlers
from dotenv import load_dotenv
import os


from dispatcher import dp
from databaseConnection import connection

load_dotenv()


async def main():
    
    bot = Bot(
        token = os.getenv("BOT_TOKEN"), #type: ignore
        default=DefaultBotProperties(
            parse_mode=ParseMode.HTML
        )
    )

    @dp.shutdown()
    async def onShutdown():
        connection.closeConnection()

    try:
        await dp.start_polling(bot, skip_updates=False)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    
    asyncio.run(main())