from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.content_key import ContentKey
    from ..models.content_metadata import ContentMetadata
    from ..models.content_type_5 import ContentType5
    from ..models.delta_lake_table import DeltaLakeTable
    from ..models.documentation import Documentation
    from ..models.iceberg_table_state import IcebergTableState
    from ..models.iceberg_view import IcebergView
    from ..models.namespace import Namespace
    from ..models.udf import UDF


T = TypeVar("T", bound="PutContentOperationForAContentKey")


@_attrs_define
class PutContentOperationForAContentKey:
    """Used to add new content or to update existing content.

    A new content object is created by populating the `value` field, the content-id in the content object must not be
    present (null).

    A content object is updated by populating the `value` containing the correct content-id.

    If the key for a content shall change (aka a rename), then use a `Delete` operation using the current (old) key and
    a `Put` operation using the new key with the `value` having the correct content-id. Both operations must happen in
    the same commit.

    A content object can be replaced (think: `DROP TABLE xyz` + `CREATE TABLE xyz`) with a `Delete` operation and a
    `Put` operation for a content using a `value`representing a new content object, so without a content-id, in the same
    commit.

        Attributes:
            key (ContentKey):
            content (Union['ContentType5', 'DeltaLakeTable', 'IcebergTableState', 'IcebergView', 'Namespace', 'UDF']):
            expected_content (Union['ContentType5', 'DeltaLakeTable', 'IcebergTableState', 'IcebergView', 'Namespace',
                'UDF', Unset]):
            metadata (Union[Unset, List['ContentMetadata']]):
            documentation (Union[Unset, Documentation]):
    """

    key: "ContentKey"
    content: Union["ContentType5", "DeltaLakeTable", "IcebergTableState", "IcebergView", "Namespace", "UDF"]
    expected_content: Union[
        "ContentType5", "DeltaLakeTable", "IcebergTableState", "IcebergView", "Namespace", "UDF", Unset
    ] = UNSET
    metadata: Union[Unset, List["ContentMetadata"]] = UNSET
    documentation: Union[Unset, "Documentation"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.delta_lake_table import DeltaLakeTable
        from ..models.iceberg_table_state import IcebergTableState
        from ..models.iceberg_view import IcebergView
        from ..models.namespace import Namespace
        from ..models.udf import UDF

        key = self.key.to_dict()

        content: Dict[str, Any]

        if isinstance(self.content, IcebergTableState):
            content = self.content.to_dict()

        elif isinstance(self.content, DeltaLakeTable):
            content = self.content.to_dict()

        elif isinstance(self.content, IcebergView):
            content = self.content.to_dict()

        elif isinstance(self.content, Namespace):
            content = self.content.to_dict()

        elif isinstance(self.content, UDF):
            content = self.content.to_dict()

        else:
            content = self.content.to_dict()

        expected_content: Union[Dict[str, Any], Unset]
        if isinstance(self.expected_content, Unset):
            expected_content = UNSET

        elif isinstance(self.expected_content, IcebergTableState):
            expected_content = self.expected_content.to_dict()

        elif isinstance(self.expected_content, DeltaLakeTable):
            expected_content = self.expected_content.to_dict()

        elif isinstance(self.expected_content, IcebergView):
            expected_content = self.expected_content.to_dict()

        elif isinstance(self.expected_content, Namespace):
            expected_content = self.expected_content.to_dict()

        elif isinstance(self.expected_content, UDF):
            expected_content = self.expected_content.to_dict()

        else:
            expected_content = self.expected_content.to_dict()

        metadata: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = []
            for metadata_item_data in self.metadata:
                metadata_item = metadata_item_data.to_dict()

                metadata.append(metadata_item)

        documentation: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.documentation, Unset):
            documentation = self.documentation.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "key": key,
                "content": content,
            }
        )
        if expected_content is not UNSET:
            field_dict["expectedContent"] = expected_content
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if documentation is not UNSET:
            field_dict["documentation"] = documentation

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.content_key import ContentKey
        from ..models.content_metadata import ContentMetadata
        from ..models.content_type_5 import ContentType5
        from ..models.delta_lake_table import DeltaLakeTable
        from ..models.documentation import Documentation
        from ..models.iceberg_table_state import IcebergTableState
        from ..models.iceberg_view import IcebergView
        from ..models.namespace import Namespace
        from ..models.udf import UDF

        d = src_dict.copy()
        key = ContentKey.from_dict(d.pop("key"))

        def _parse_content(
            data: object,
        ) -> Union["ContentType5", "DeltaLakeTable", "IcebergTableState", "IcebergView", "Namespace", "UDF"]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_content_type_0 = IcebergTableState.from_dict(data)

                return componentsschemas_content_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_content_type_1 = DeltaLakeTable.from_dict(data)

                return componentsschemas_content_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_content_type_2 = IcebergView.from_dict(data)

                return componentsschemas_content_type_2
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_content_type_3 = Namespace.from_dict(data)

                return componentsschemas_content_type_3
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_content_type_4 = UDF.from_dict(data)

                return componentsschemas_content_type_4
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_content_type_5 = ContentType5.from_dict(data)

            return componentsschemas_content_type_5

        content = _parse_content(d.pop("content"))

        def _parse_expected_content(
            data: object,
        ) -> Union["ContentType5", "DeltaLakeTable", "IcebergTableState", "IcebergView", "Namespace", "UDF", Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_content_type_0 = IcebergTableState.from_dict(data)

                return componentsschemas_content_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_content_type_1 = DeltaLakeTable.from_dict(data)

                return componentsschemas_content_type_1
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_content_type_2 = IcebergView.from_dict(data)

                return componentsschemas_content_type_2
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_content_type_3 = Namespace.from_dict(data)

                return componentsschemas_content_type_3
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_content_type_4 = UDF.from_dict(data)

                return componentsschemas_content_type_4
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_content_type_5 = ContentType5.from_dict(data)

            return componentsschemas_content_type_5

        expected_content = _parse_expected_content(d.pop("expectedContent", UNSET))

        metadata = []
        _metadata = d.pop("metadata", UNSET)
        for metadata_item_data in _metadata or []:
            metadata_item = ContentMetadata.from_dict(metadata_item_data)

            metadata.append(metadata_item)

        _documentation = d.pop("documentation", UNSET)
        documentation: Union[Unset, Documentation]
        if isinstance(_documentation, Unset):
            documentation = UNSET
        else:
            documentation = Documentation.from_dict(_documentation)

        put_content_operation_for_a_content_key = cls(
            key=key,
            content=content,
            expected_content=expected_content,
            metadata=metadata,
            documentation=documentation,
        )

        put_content_operation_for_a_content_key.additional_properties = d
        return put_content_operation_for_a_content_key

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
