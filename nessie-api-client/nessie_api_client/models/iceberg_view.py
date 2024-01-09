from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.iceberg_view_metadata import IcebergViewMetadata


T = TypeVar("T", bound="IcebergView")


@_attrs_define
class IcebergView:
    """
    Attributes:
        metadata_location (str):
        sql_text (str):
        id (Union[Unset, str]):
        version_id (Union[Unset, int]):
        schema_id (Union[Unset, int]):
        dialect (Union[Unset, str]):
        metadata (Union[Unset, IcebergViewMetadata]):
    """

    metadata_location: str
    sql_text: str
    id: Union[Unset, str] = UNSET
    version_id: Union[Unset, int] = UNSET
    schema_id: Union[Unset, int] = UNSET
    dialect: Union[Unset, str] = UNSET
    metadata: Union[Unset, "IcebergViewMetadata"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        metadata_location = self.metadata_location
        sql_text = self.sql_text
        id = self.id
        version_id = self.version_id
        schema_id = self.schema_id
        dialect = self.dialect
        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "metadataLocation": metadata_location,
                "sqlText": sql_text,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if version_id is not UNSET:
            field_dict["versionId"] = version_id
        if schema_id is not UNSET:
            field_dict["schemaId"] = schema_id
        if dialect is not UNSET:
            field_dict["dialect"] = dialect
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.iceberg_view_metadata import IcebergViewMetadata

        d = src_dict.copy()
        metadata_location = d.pop("metadataLocation")

        sql_text = d.pop("sqlText")

        id = d.pop("id", UNSET)

        version_id = d.pop("versionId", UNSET)

        schema_id = d.pop("schemaId", UNSET)

        dialect = d.pop("dialect", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, IcebergViewMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = IcebergViewMetadata.from_dict(_metadata)

        iceberg_view = cls(
            metadata_location=metadata_location,
            sql_text=sql_text,
            id=id,
            version_id=version_id,
            schema_id=schema_id,
            dialect=dialect,
            metadata=metadata,
        )

        iceberg_view.additional_properties = d
        return iceberg_view

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
