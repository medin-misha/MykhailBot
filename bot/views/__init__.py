from aiogram import Router
from .base_commands.views import router as base_commands_router

__all__ = "router"
router = Router()
router.include_routers(base_commands_router)
