from sqlmodel import SQLModel, Field
from datetime import datetime

class Users(SQLModel, table=True):
    user_id: int = Field(default=None, primary_key=True)
    username: str
    email: str
    created_at: datetime = Field(default=None)