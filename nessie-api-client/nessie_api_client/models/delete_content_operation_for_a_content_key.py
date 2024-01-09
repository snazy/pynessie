from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.content_key import ContentKey


T = TypeVar("T", bound="DeleteContentOperationForAContentKey")


@_attrs_define
class DeleteContentOperationForAContentKey:
    """Used to delete an existing content key.

    If the key for a content shall change (aka a rename), then use a `Delete` operation using the current (old) key and
    a `Put` operation using the new key with the current `Content` in the the `value` field. See `Put` operation.

        Attributes:
            key (ContentKey):
    """

    key: "ContentKey"
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        key = self.key.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key": key,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.content_key import ContentKey

        d = src_dict.copy()
        key = ContentKey.from_dict(d.pop("key"))

        delete_content_operation_for_a_content_key = cls(
            key=key,
        )

        delete_content_operation_for_a_content_key.additional_properties = d
        return delete_content_operation_for_a_content_key

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
