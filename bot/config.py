import dotenv
from pathlib import Path, PosixPath
import os

class BaseSettings:
    base_dir: PosixPath = Path.cwd()

dotenv.load_dotenv(BaseSettings.base_dir / ".env")


class BotSettings:
    token: str = os.getenv("TOKEN")

