from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


class ReplayKeyboards:
    @staticmethod
    def kb_start() -> ReplyKeyboardMarkup:
        line1: list[KeyboardButton] = [KeyboardButton(text=text) for text in ["/table"]]
        return ReplyKeyboardMarkup(keyboard=[line1])
