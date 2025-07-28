from typing import Sequence


class MassAssignableMixin:
    __fillable__: Sequence[str] = []

    def fill(self, data: dict):
        for field in self.__fillable__:
            if field in data:
                setattr(self, field, data[field])
