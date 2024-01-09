from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DeltaLakeTableV1")


@_attrs_define
class DeltaLakeTableV1:
    """
    Attributes:
        metadata_location_history (List[str]):
        checkpoint_location_history (List[str]):
        id (Union[Unset, str]):
        last_checkpoint (Union[Unset, str]):
    """

    metadata_location_history: List[str]
    checkpoint_location_history: List[str]
    id: Union[Unset, str] = UNSET
    last_checkpoint: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        metadata_location_history = self.metadata_location_history

        checkpoint_location_history = self.checkpoint_location_history

        id = self.id
        last_checkpoint = self.last_checkpoint

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "metadataLocationHistory": metadata_location_history,
                "checkpointLocationHistory": checkpoint_location_history,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if last_checkpoint is not UNSET:
            field_dict["lastCheckpoint"] = last_checkpoint

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        metadata_location_history = cast(List[str], d.pop("metadataLocationHistory"))

        checkpoint_location_history = cast(List[str], d.pop("checkpointLocationHistory"))

        id = d.pop("id", UNSET)

        last_checkpoint = d.pop("lastCheckpoint", UNSET)

        delta_lake_table_v1 = cls(
            metadata_location_history=metadata_location_history,
            checkpoint_location_history=checkpoint_location_history,
            id=id,
            last_checkpoint=last_checkpoint,
        )

        delta_lake_table_v1.additional_properties = d
        return delta_lake_table_v1

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
