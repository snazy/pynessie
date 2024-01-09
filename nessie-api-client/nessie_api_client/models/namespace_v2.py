from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.namespace_v2_properties import NamespaceV2Properties


T = TypeVar("T", bound="NamespaceV2")


@_attrs_define
class NamespaceV2:
    """
    Attributes:
        elements (List[str]):
        properties (NamespaceV2Properties):
        id (Union[Unset, str]):
    """

    elements: List[str]
    properties: "NamespaceV2Properties"
    id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        elements = self.elements

        properties = self.properties.to_dict()

        id = self.id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "elements": elements,
                "properties": properties,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.namespace_v2_properties import NamespaceV2Properties

        d = src_dict.copy()
        elements = cast(List[str], d.pop("elements"))

        properties = NamespaceV2Properties.from_dict(d.pop("properties"))

        id = d.pop("id", UNSET)

        namespace_v2 = cls(
            elements=elements,
            properties=properties,
            id=id,
        )

        namespace_v2.additional_properties = d
        return namespace_v2

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
