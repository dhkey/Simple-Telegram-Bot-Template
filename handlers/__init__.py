from dispatcher import dp

from . import personal_actions

dp.include_router(personal_actions.router)