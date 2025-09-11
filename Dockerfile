FROM ghcr.io/astral-sh/uv:python3.13-bookworm

LABEL creator = "@medin-misha"

COPY pyproject.toml .
COPY bot bot/
WORKDIR bot/
CMD ["uv", "run", "main.py"]