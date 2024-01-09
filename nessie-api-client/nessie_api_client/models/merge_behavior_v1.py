from enum import Enum


class MergeBehaviorV1(str, Enum):
    DROP = "DROP"
    FORCE = "FORCE"
    NORMAL = "NORMAL"

    def __str__(self) -> str:
        return str(self.value)
