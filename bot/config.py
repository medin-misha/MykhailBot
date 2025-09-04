import dotenv
from pathlib import Path, PosixPath
import os

class BaseSettings:
    base_dir: PosixPath = Path.cwd()

dotenv.load_dotenv(BaseSettings.base_dir / ".env")


class BotSettings:
    token: str = os.getenv("TOKEN")

class Messages:
    start: str = os.getenv("START_MESSAGE") or "Привет, я бот который создаст твою <b>личную</b> таблицу жизни! Напиши мне /table что бы начать процесс создания."
