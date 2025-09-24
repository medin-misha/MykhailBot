import json
from views.amqp_broker import broker
from config import QueueSettings


async def save_user(chat_id: int, username: str):
    message: dict = {"chat_id": chat_id, "username": username}
    raw_message: str = json.dumps(message)
    await broker.publish(message=raw_message, queue=QueueSettings.auth_queue)
