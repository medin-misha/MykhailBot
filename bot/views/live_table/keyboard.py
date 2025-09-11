from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def build_info_kb() -> InlineKeyboardMarkup:
    tg_channel = InlineKeyboardButton(text="Канал", url="https://t.me/medinmisha")
    row = [tg_channel]
    # список из списков (Двумерный массив)
    rows = [row]
    return InlineKeyboardMarkup(inline_keyboard=rows)