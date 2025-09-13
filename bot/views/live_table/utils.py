from aiogram.types import Message, BufferedInputFile

from datetime import datetime
from typing import Optional, Dict
import io

from utils.print_live_table import LiveTableDraw

def validate_date_format(date: str, format: str = "%d/%m/%Y") -> Optional[str]:
    """Проверка формата даты из строки date"""
    try:
        datetime.strptime(date, format)
        return None
    except ValueError as ext:
        print(ext)
        return f"Неверный формат даты {ext}"


def create_table(date: str, username: str) -> Dict[str, io.BytesIO | None | str | list]:
    """Функция создающая файл с таблицей. Возвращает словарь с таблицей, статусом создания, и ошибками."""
    errors = []
    date_error = validate_date_format(date=date)
    if date_error:
        errors.append(date_error)
        return {"table": None, "is_created": False, "errors": errors}
    table = LiveTableDraw(name=username, birthday_date=date)
    table_image = table.create_table()
    return {"table": table_image, "is_created": True, "errors": errors}




async def send_table_or_error(table_data: Dict[str, io.BytesIO | None | str | list], msg: Message) -> None:
    """Функция которая скидывает таблицу в чат пользователю или
    оправляет ему сообщение об ошибке формата введённой им даты"""
    if table_data.get("errors"):
        print(table_data)
        await msg.answer("Ты скинул что то не то, формат даты должен быть <b>03/09/2008</b>.")
        return None

    await msg.bot.send_document(
        chat_id=msg.chat.id,
        document=BufferedInputFile(
            file=table_data["table"].getvalue(),
            filename="table.png"
        )
    )
    return None
