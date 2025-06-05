import asyncio
import structlog
from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from dispatcher import dp
from databaseConnection import connection
import handlers
from dotenv import load_dotenv
import os

load_dotenv()

async def main():
    
    bot = Bot(
        token = os.getenv("BOT_TOKEN"), #type: ignore
        default=DefaultBotProperties(
            parse_mode=ParseMode.HTML
        )
    )

    print("Starting the bot...")

    @dp.startup()
    async def onSturtup():
        print("BOT ::: Started ✅")

    @dp.shutdown()
    async def onShutdown():
        connection.closeConnection()

    try:
        await dp.start_polling(bot, skip_updates=False)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(main())