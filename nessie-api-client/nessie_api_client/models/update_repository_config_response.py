from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.garbage_collector_config_object import GarbageCollectorConfigObject


T = TypeVar("T", bound="UpdateRepositoryConfigResponse")


@_attrs_define
class UpdateRepositoryConfigResponse:
    """
    Attributes:
        previous (Union[Unset, GarbageCollectorConfigObject]):
    """

    previous: Union[Unset, "GarbageCollectorConfigObject"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        previous: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.previous, Unset):
            previous = self.previous.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if previous is not UNSET:
            field_dict["previous"] = previous

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.garbage_collector_config_object import GarbageCollectorConfigObject

        d = src_dict.copy()
        _previous = d.pop("previous", UNSET)
        previous: Union[Unset, GarbageCollectorConfigObject]
        if isinstance(_previous, Unset):
            previous = UNSET
        else:
            previous = GarbageCollectorConfigObject.from_dict(_previous)

        update_repository_config_response = cls(
            previous=previous,
        )

        update_repository_config_response.additional_properties = d
        return update_repository_config_response

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
