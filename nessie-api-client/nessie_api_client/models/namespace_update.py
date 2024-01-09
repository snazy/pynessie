from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.namespace_update_property_updates import NamespaceUpdatePropertyUpdates


T = TypeVar("T", bound="NamespaceUpdate")


@_attrs_define
class NamespaceUpdate:
    """
    Attributes:
        property_updates (Union[Unset, NamespaceUpdatePropertyUpdates]):
        property_removals (Union[Unset, List[str]]):
    """

    property_updates: Union[Unset, "NamespaceUpdatePropertyUpdates"] = UNSET
    property_removals: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        property_updates: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.property_updates, Unset):
            property_updates = self.property_updates.to_dict()

        property_removals: Union[Unset, List[str]] = UNSET
        if not isinstance(self.property_removals, Unset):
            property_removals = self.property_removals

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if property_updates is not UNSET:
            field_dict["propertyUpdates"] = property_updates
        if property_removals is not UNSET:
            field_dict["propertyRemovals"] = property_removals

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.namespace_update_property_updates import NamespaceUpdatePropertyUpdates

        d = src_dict.copy()
        _property_updates = d.pop("propertyUpdates", UNSET)
        property_updates: Union[Unset, NamespaceUpdatePropertyUpdates]
        if isinstance(_property_updates, Unset):
            property_updates = UNSET
        else:
            property_updates = NamespaceUpdatePropertyUpdates.from_dict(_property_updates)

        property_removals = cast(List[str], d.pop("propertyRemovals", UNSET))

        namespace_update = cls(
            property_updates=property_updates,
            property_removals=property_removals,
        )

        namespace_update.additional_properties = d
        return namespace_update

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
