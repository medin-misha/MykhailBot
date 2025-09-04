import dotenv
from pathlib import Path, PosixPath
import os

class BaseSettings:
    base_dir: PosixPath = Path.cwd()

dotenv.load_dotenv(BaseSettings.base_dir / ".env")


class BotSettings:
    token: str = os.getenv("TOKEN")

class Messages:
    start: str = os.getenv("START_MESSAGE", "Привет, я бот который создаст твою <b>личную</b> таблицу жизни! Напиши мне /table что бы начать процесс создания.")
    social: str = os.getenv("SOCIAL_MESSAGE", "Вот все мои медиа &lt;3")
    media_links: dict = {
        "YouTube": os.getenv("YOUTUBE_LINK", "https://www.youtube.com/@it_was_I_misha"),
        "Telegram": os.getenv("TELEGRAM_LINK", "https://t.me/medinmisha"),
        "Instagram": os.getenv("INSTAGRAM_LINK", "https://www.instagram.com/it_was_i_misha/"),
        "TikTok": os.getenv("TIKTOK_LINK", "https://www.tiktok.com/@iteasimisha"),
        "VK": os.getenv("VK_LINK", "https://vk.com/id766354665"),
    }