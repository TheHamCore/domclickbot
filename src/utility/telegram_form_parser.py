from pydantic import BaseModel, Field


class ChatInfo(BaseModel):
    telegram_chat_id: int = Field(alias='id')
    first_name: str
    username: str = None


class MessageInfo(BaseModel):
    chat: ChatInfo
    text: str


class UserInfo(BaseModel):
    message: MessageInfo
