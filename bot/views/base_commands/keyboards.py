from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from config import Messages


class ReplyKeyboards:
    @staticmethod
    def kb_start() -> ReplyKeyboardMarkup:
        line1: list[KeyboardButton] = [
            KeyboardButton(text=text) for text in ["/table", "/social"]
        ]
        return ReplyKeyboardMarkup(keyboard=[line1], resize_keyboard=True)

    @staticmethod
    def kb_social() -> InlineKeyboardMarkup:
        builder = InlineKeyboardBuilder()

        for name, link in Messages.media_links.items():
            builder.button(text=name, url=link)
        builder.adjust(2)
        return builder.as_markup(resize_keyboard=True)
