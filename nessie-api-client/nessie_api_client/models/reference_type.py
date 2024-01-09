from enum import Enum


class ReferenceType(str, Enum):
    BRANCH = "branch"
    TAG = "tag"

    def __str__(self) -> str:
        return str(self.value)
