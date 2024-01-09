from enum import Enum


class MergeBehavior(str, Enum):
    DROP = "DROP"
    FORCE = "FORCE"
    NORMAL = "NORMAL"

    def __str__(self) -> str:
        return str(self.value)
