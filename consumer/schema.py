from pydantic import BaseModel
from pydantic import Field


class PingHost(BaseModel):
    host: str = Field(description="Host")


class TelegramSendMessage(BaseModel):
    chat_id: int = Field()
    text: str = Field()
