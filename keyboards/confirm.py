from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton


def get_start_keyboard(localization) -> InlineKeyboardMarkup:
    kb = [
        [KeyboardButton(text=localization.gettext("confirm"))]
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=kb)
    return keyboard
