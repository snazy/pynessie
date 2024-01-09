from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.content_key_v1 import ContentKeyV1


T = TypeVar("T", bound="EntryV1")


@_attrs_define
class EntryV1:
    """
    Attributes:
        name (ContentKeyV1):
        type (Union[Unset, str]): Declares the type of a Nessie content object, which is currently one of ICEBERG_TABLE,
            DELTA_LAKE_TABLE, ICEBERG_VIEW, NAMESPACE or UDF, which are the discriminator mapping values of the 'Content'
            type.
    """

    name: "ContentKeyV1"
    type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name.to_dict()

        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.content_key_v1 import ContentKeyV1

        d = src_dict.copy()
        name = ContentKeyV1.from_dict(d.pop("name"))

        type = d.pop("type", UNSET)

        entry_v1 = cls(
            name=name,
            type=type,
        )

        entry_v1.additional_properties = d
        return entry_v1

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
