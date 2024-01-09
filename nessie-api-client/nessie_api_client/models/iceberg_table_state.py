from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.iceberg_table_state_metadata import IcebergTableStateMetadata


T = TypeVar("T", bound="IcebergTableState")


@_attrs_define
class IcebergTableState:
    """Represents the state of an Iceberg table in Nessie. An Iceberg table is globally identified via its unique
    'Content.id'.

    A Nessie commit-operation, performed via 'TreeApi.commitMultipleOperations',for Iceberg consists of a
    'Operation.Put' with an 'IcebergTable' as in the 'content' field and the previous value of 'IcebergTable' in the
    'expectedContent' field.

        Attributes:
            metadata_location (str):
            id (Union[Unset, str]):
            snapshot_id (Union[Unset, int]):
            schema_id (Union[Unset, int]):
            spec_id (Union[Unset, int]):
            sort_order_id (Union[Unset, int]):
            metadata (Union[Unset, IcebergTableStateMetadata]):
    """

    metadata_location: str
    id: Union[Unset, str] = UNSET
    snapshot_id: Union[Unset, int] = UNSET
    schema_id: Union[Unset, int] = UNSET
    spec_id: Union[Unset, int] = UNSET
    sort_order_id: Union[Unset, int] = UNSET
    metadata: Union[Unset, "IcebergTableStateMetadata"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        metadata_location = self.metadata_location
        id = self.id
        snapshot_id = self.snapshot_id
        schema_id = self.schema_id
        spec_id = self.spec_id
        sort_order_id = self.sort_order_id
        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "metadataLocation": metadata_location,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if snapshot_id is not UNSET:
            field_dict["snapshotId"] = snapshot_id
        if schema_id is not UNSET:
            field_dict["schemaId"] = schema_id
        if spec_id is not UNSET:
            field_dict["specId"] = spec_id
        if sort_order_id is not UNSET:
            field_dict["sortOrderId"] = sort_order_id
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.iceberg_table_state_metadata import IcebergTableStateMetadata

        d = src_dict.copy()
        metadata_location = d.pop("metadataLocation")

        id = d.pop("id", UNSET)

        snapshot_id = d.pop("snapshotId", UNSET)

        schema_id = d.pop("schemaId", UNSET)

        spec_id = d.pop("specId", UNSET)

        sort_order_id = d.pop("sortOrderId", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, IcebergTableStateMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = IcebergTableStateMetadata.from_dict(_metadata)

        iceberg_table_state = cls(
            metadata_location=metadata_location,
            id=id,
            snapshot_id=snapshot_id,
            schema_id=schema_id,
            spec_id=spec_id,
            sort_order_id=sort_order_id,
            metadata=metadata,
        )

        iceberg_table_state.additional_properties = d
        return iceberg_table_state

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
