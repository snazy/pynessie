from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.log_entry import LogEntry


T = TypeVar("T", bound="LogResponse")


@_attrs_define
class LogResponse:
    """
    Attributes:
        log_entries (List['LogEntry']):
        has_more (Union[Unset, bool]):
        token (Union[Unset, str]):
    """

    log_entries: List["LogEntry"]
    has_more: Union[Unset, bool] = UNSET
    token: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        log_entries = []
        for log_entries_item_data in self.log_entries:
            log_entries_item = log_entries_item_data.to_dict()

            log_entries.append(log_entries_item)

        has_more = self.has_more
        token = self.token

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "logEntries": log_entries,
            }
        )
        if has_more is not UNSET:
            field_dict["hasMore"] = has_more
        if token is not UNSET:
            field_dict["token"] = token

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.log_entry import LogEntry

        d = src_dict.copy()
        log_entries = []
        _log_entries = d.pop("logEntries")
        for log_entries_item_data in _log_entries:
            log_entries_item = LogEntry.from_dict(log_entries_item_data)

            log_entries.append(log_entries_item)

        has_more = d.pop("hasMore", UNSET)

        token = d.pop("token", UNSET)

        log_response = cls(
            log_entries=log_entries,
            has_more=has_more,
            token=token,
        )

        log_response.additional_properties = d
        return log_response

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
