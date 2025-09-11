from aiogram import Router
from .base_commands.views import router as base_commands_router
from .live_table.views import router as live_table_router

__all__ = "router"
router = Router()
router.include_routers(base_commands_router, live_table_router)
