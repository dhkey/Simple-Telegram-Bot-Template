import structlog
from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

router = Router()
router.message.filter(F.chat.type == "private")

logger = structlog.get_logger()

@router.message(Command("start"))
async def start_command_handler(message: Message, localization, state: FSMContext):
    
    await message.answer(localization.gettext("welcome-message"))