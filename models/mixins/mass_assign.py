from typing import Sequence
from wtforms.fields import Field


class MassAssignableMixin:
    __fillable__: Sequence[str] = []

    def fill(self, data: dict):
        for field in self.__fillable__:
            if field in data:
                if isinstance(data[field], Field):
                    setattr(self, field, data[field].data)
                else:
                    setattr(self, field, data[field])
