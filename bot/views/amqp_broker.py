from faststream.rabbit import RabbitBroker
from faststream import FastStream
from config import BotSettings

broker = RabbitBroker(BotSettings.rmq_url)
app = FastStream(broker)
