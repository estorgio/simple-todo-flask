from extensions.database import Base
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
from sqlalchemy import DateTime, Text
from models.mixins.mass_assign import MassAssignableMixin


class Todo(MassAssignableMixin, Base):
    __tablename__ = 'todos'
    __fillable__ = ['text', 'is_done']

    id: Mapped[int] = mapped_column(primary_key=True)
    text: Mapped[str] = mapped_column(Text)
    added_on: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.now)
    is_done: Mapped[bool] = mapped_column(default=False)

    def __repr__(self):
        return f'Todo(text="{self.text}", added_on="{self.added_on}", is_done="{self.is_done}")'
