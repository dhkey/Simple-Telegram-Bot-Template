from typing import Callable, Dict, Any, Awaitable
from aiogram import BaseMiddleware
from aiogram.types import Message
from aiogram.utils.i18n import I18n
from pathlib import Path
from database.userDatabase import User
import json 

current_dir = Path(__file__).parent
locales_path = current_dir.parent / "locales"

default_locale = "en"

class LocalizationMiddleware(BaseMiddleware):
    def __init__(self):
        super().__init__()

    async def __call__( #type: ignore
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any]
    ) -> Any:
        
        user_id = event.from_user.id #type: ignore
        self.user = User(user_id)
        
        user_locale = self.get_user_locale() if self.user.isUserInDatabase() else default_locale
        
        with open(f"{locales_path}/{user_locale}.json") as locale_file:
            localization = json.load(locale_file)
            
        data["localization"] = localization
        return await handler(event, data)

    def get_user_locale(self) -> str:
        userConnectionStructure = self.user.getUserLanguageCode()
        return userConnectionStructure if userConnectionStructure is not None else "ru"
