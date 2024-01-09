from enum import Enum


class CommitConsistency(str, Enum):
    COMMIT_CONSISTENT = "COMMIT_CONSISTENT"
    COMMIT_CONTENT_INCONSISTENT = "COMMIT_CONTENT_INCONSISTENT"
    COMMIT_INCONSISTENT = "COMMIT_INCONSISTENT"
    NOT_CHECKED = "NOT_CHECKED"

    def __str__(self) -> str:
        return str(self.value)
