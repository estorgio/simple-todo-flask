from extensions.database import Base
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
from sqlalchemy import DateTime


class Todo(Base):
    __tablename__ = 'todos'
    allowed_fields = ['text', 'is_done']

    id: Mapped[int] = mapped_column(primary_key=True)
    text: Mapped[str]
    added_on: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.now)
    is_done: Mapped[bool] = mapped_column(default=False)

    def __repr__(self):
        return f'Todo(text="{self.text}", added_on="{self.added_on}", is_done="{self.is_done}")'
