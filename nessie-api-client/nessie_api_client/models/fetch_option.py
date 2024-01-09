from enum import Enum


class FetchOption(str, Enum):
    ALL = "ALL"
    MINIMAL = "MINIMAL"

    def __str__(self) -> str:
        return str(self.value)
