from enum import Enum


class MergeBehaviorV2(str, Enum):
    DROP = "DROP"
    FORCE = "FORCE"
    NORMAL = "NORMAL"

    def __str__(self) -> str:
        return str(self.value)
