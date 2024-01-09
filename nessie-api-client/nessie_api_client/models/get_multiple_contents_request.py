from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.content_key import ContentKey


T = TypeVar("T", bound="GetMultipleContentsRequest")


@_attrs_define
class GetMultipleContentsRequest:
    """
    Attributes:
        requested_keys (List['ContentKey']):
    """

    requested_keys: List["ContentKey"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        requested_keys = []
        for requested_keys_item_data in self.requested_keys:
            requested_keys_item = requested_keys_item_data.to_dict()

            requested_keys.append(requested_keys_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "requestedKeys": requested_keys,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.content_key import ContentKey

        d = src_dict.copy()
        requested_keys = []
        _requested_keys = d.pop("requestedKeys")
        for requested_keys_item_data in _requested_keys:
            requested_keys_item = ContentKey.from_dict(requested_keys_item_data)

            requested_keys.append(requested_keys_item)

        get_multiple_contents_request = cls(
            requested_keys=requested_keys,
        )

        get_multiple_contents_request.additional_properties = d
        return get_multiple_contents_request

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
