from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from database.userDatabase import User

router = Router()
router.message.filter(F.chat.type == "private")

@router.message(Command("start"))
async def start_command_handler(message: Message, localization, state: FSMContext):
    
    user = User(message.from_user.id) #type: ignore
    user.createNewUser()
    
    await message.answer(localization["start_message"], parse_mode="HTML")