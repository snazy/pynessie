from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.namespace_v1_properties import NamespaceV1Properties


T = TypeVar("T", bound="NamespaceV1")


@_attrs_define
class NamespaceV1:
    """
    Attributes:
        elements (List[str]):
        properties (NamespaceV1Properties):
        id (Union[Unset, str]):
    """

    elements: List[str]
    properties: "NamespaceV1Properties"
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
        from ..models.namespace_v1_properties import NamespaceV1Properties

        d = src_dict.copy()
        elements = cast(List[str], d.pop("elements"))

        properties = NamespaceV1Properties.from_dict(d.pop("properties"))

        id = d.pop("id", UNSET)

        namespace_v1 = cls(
            elements=elements,
            properties=properties,
            id=id,
        )

        namespace_v1.additional_properties = d
        return namespace_v1

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
