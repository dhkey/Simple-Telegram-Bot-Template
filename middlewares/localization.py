from typing import Callable, Dict, Any, Awaitable
from aiogram import BaseMiddleware
from aiogram.types import Message
from aiogram.utils.i18n import I18n
from pathlib import Path
from database.userDatabase import User

current_dir = Path(__file__).parent
locales_path = current_dir.parent / "locales"

i18n = I18n(path=str(locales_path), default_locale="en", domain="messages")

class LocalizationMiddleware(BaseMiddleware):
    def __init__(self):
        super().__init__()
        self.i18n = i18n

    async def __call__(
        self,
        handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
        event: Message,
        data: Dict[str, Any]
    ) -> Any:
        
        user_id = event.from_user.id
        self.user = User(user_id)
        
        user_locale = self.get_user_locale()
        
        self.i18n.ctx_locale.set(user_locale)    
        
        data["localization"] = self.i18n
        return await handler(event, data)

    def get_user_locale(self) -> str:
        userConnectionStructure = self.user.getUserLanguageCode()
        return userConnectionStructure if userConnectionStructure is not None else "ru"
