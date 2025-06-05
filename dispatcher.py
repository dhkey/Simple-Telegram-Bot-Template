from aiogram import Dispatcher
from middlewares.localization import LocalizationMiddleware

dp = Dispatcher()

localization_middleware = LocalizationMiddleware()

dp.message.outer_middleware(localization_middleware)
dp.callback_query.outer_middleware(localization_middleware)
dp.inline_query.outer_middleware(localization_middleware)