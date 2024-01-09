from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.entry_v1 import EntryV1


T = TypeVar("T", bound="EntriesResponseV1")


@_attrs_define
class EntriesResponseV1:
    """
    Attributes:
        entries (List['EntryV1']):
        has_more (Union[Unset, bool]):
        token (Union[Unset, str]):
    """

    entries: List["EntryV1"]
    has_more: Union[Unset, bool] = UNSET
    token: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        entries = []
        for entries_item_data in self.entries:
            entries_item = entries_item_data.to_dict()

            entries.append(entries_item)

        has_more = self.has_more
        token = self.token

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "entries": entries,
            }
        )
        if has_more is not UNSET:
            field_dict["hasMore"] = has_more
        if token is not UNSET:
            field_dict["token"] = token

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.entry_v1 import EntryV1

        d = src_dict.copy()
        entries = []
        _entries = d.pop("entries")
        for entries_item_data in _entries:
            entries_item = EntryV1.from_dict(entries_item_data)

            entries.append(entries_item)

        has_more = d.pop("hasMore", UNSET)

        token = d.pop("token", UNSET)

        entries_response_v1 = cls(
            entries=entries,
            has_more=has_more,
            token=token,
        )

        entries_response_v1.additional_properties = d
        return entries_response_v1

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
