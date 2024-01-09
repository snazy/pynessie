from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.namespace_v1 import NamespaceV1


T = TypeVar("T", bound="GetNamespacesResponseV1")


@_attrs_define
class GetNamespacesResponseV1:
    """
    Attributes:
        namespaces (List['NamespaceV1']):
    """

    namespaces: List["NamespaceV1"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        namespaces = []
        for namespaces_item_data in self.namespaces:
            namespaces_item = namespaces_item_data.to_dict()

            namespaces.append(namespaces_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "namespaces": namespaces,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.namespace_v1 import NamespaceV1

        d = src_dict.copy()
        namespaces = []
        _namespaces = d.pop("namespaces")
        for namespaces_item_data in _namespaces:
            namespaces_item = NamespaceV1.from_dict(namespaces_item_data)

            namespaces.append(namespaces_item)

        get_namespaces_response_v1 = cls(
            namespaces=namespaces,
        )

        get_namespaces_response_v1.additional_properties = d
        return get_namespaces_response_v1

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
