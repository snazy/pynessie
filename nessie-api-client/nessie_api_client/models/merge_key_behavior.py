from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.merge_behavior import MergeBehavior
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


T = TypeVar("T", bound="MergeKeyBehavior")


@_attrs_define
class MergeKeyBehavior:
    """
    Attributes:
        key (Union[Unset, ContentKey]):
        merge_behavior (Union[Unset, MergeBehavior]):
        expected_target_content (Union['ContentType5', 'DeltaLakeTable', 'IcebergTableState', 'IcebergView',
            'Namespace', 'UDF', Unset]):
        resolved_content (Union['ContentType5', 'DeltaLakeTable', 'IcebergTableState', 'IcebergView', 'Namespace',
            'UDF', Unset]):
        expected_target_documentation (Union[Unset, Documentation]):
        resolved_documentation (Union[Unset, Documentation]):
        metadata (Union[Unset, List['ContentMetadata']]):
    """

    key: Union[Unset, "ContentKey"] = UNSET
    merge_behavior: Union[Unset, MergeBehavior] = UNSET
    expected_target_content: Union[
        "ContentType5", "DeltaLakeTable", "IcebergTableState", "IcebergView", "Namespace", "UDF", Unset
    ] = UNSET
    resolved_content: Union[
        "ContentType5", "DeltaLakeTable", "IcebergTableState", "IcebergView", "Namespace", "UDF", Unset
    ] = UNSET
    expected_target_documentation: Union[Unset, "Documentation"] = UNSET
    resolved_documentation: Union[Unset, "Documentation"] = UNSET
    metadata: Union[Unset, List["ContentMetadata"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.delta_lake_table import DeltaLakeTable
        from ..models.iceberg_table_state import IcebergTableState
        from ..models.iceberg_view import IcebergView
        from ..models.namespace import Namespace
        from ..models.udf import UDF

        key: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.key, Unset):
            key = self.key.to_dict()

        merge_behavior: Union[Unset, str] = UNSET
        if not isinstance(self.merge_behavior, Unset):
            merge_behavior = self.merge_behavior.value

        expected_target_content: Union[Dict[str, Any], Unset]
        if isinstance(self.expected_target_content, Unset):
            expected_target_content = UNSET

        elif isinstance(self.expected_target_content, IcebergTableState):
            expected_target_content = self.expected_target_content.to_dict()

        elif isinstance(self.expected_target_content, DeltaLakeTable):
            expected_target_content = self.expected_target_content.to_dict()

        elif isinstance(self.expected_target_content, IcebergView):
            expected_target_content = self.expected_target_content.to_dict()

        elif isinstance(self.expected_target_content, Namespace):
            expected_target_content = self.expected_target_content.to_dict()

        elif isinstance(self.expected_target_content, UDF):
            expected_target_content = self.expected_target_content.to_dict()

        else:
            expected_target_content = self.expected_target_content.to_dict()

        resolved_content: Union[Dict[str, Any], Unset]
        if isinstance(self.resolved_content, Unset):
            resolved_content = UNSET

        elif isinstance(self.resolved_content, IcebergTableState):
            resolved_content = self.resolved_content.to_dict()

        elif isinstance(self.resolved_content, DeltaLakeTable):
            resolved_content = self.resolved_content.to_dict()

        elif isinstance(self.resolved_content, IcebergView):
            resolved_content = self.resolved_content.to_dict()

        elif isinstance(self.resolved_content, Namespace):
            resolved_content = self.resolved_content.to_dict()

        elif isinstance(self.resolved_content, UDF):
            resolved_content = self.resolved_content.to_dict()

        else:
            resolved_content = self.resolved_content.to_dict()

        expected_target_documentation: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.expected_target_documentation, Unset):
            expected_target_documentation = self.expected_target_documentation.to_dict()

        resolved_documentation: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.resolved_documentation, Unset):
            resolved_documentation = self.resolved_documentation.to_dict()

        metadata: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = []
            for metadata_item_data in self.metadata:
                metadata_item = metadata_item_data.to_dict()

                metadata.append(metadata_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if key is not UNSET:
            field_dict["key"] = key
        if merge_behavior is not UNSET:
            field_dict["mergeBehavior"] = merge_behavior
        if expected_target_content is not UNSET:
            field_dict["expectedTargetContent"] = expected_target_content
        if resolved_content is not UNSET:
            field_dict["resolvedContent"] = resolved_content
        if expected_target_documentation is not UNSET:
            field_dict["expectedTargetDocumentation"] = expected_target_documentation
        if resolved_documentation is not UNSET:
            field_dict["resolvedDocumentation"] = resolved_documentation
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

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
        _key = d.pop("key", UNSET)
        key: Union[Unset, ContentKey]
        if isinstance(_key, Unset):
            key = UNSET
        else:
            key = ContentKey.from_dict(_key)

        _merge_behavior = d.pop("mergeBehavior", UNSET)
        merge_behavior: Union[Unset, MergeBehavior]
        if isinstance(_merge_behavior, Unset):
            merge_behavior = UNSET
        else:
            merge_behavior = MergeBehavior(_merge_behavior)

        def _parse_expected_target_content(
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

        expected_target_content = _parse_expected_target_content(d.pop("expectedTargetContent", UNSET))

        def _parse_resolved_content(
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

        resolved_content = _parse_resolved_content(d.pop("resolvedContent", UNSET))

        _expected_target_documentation = d.pop("expectedTargetDocumentation", UNSET)
        expected_target_documentation: Union[Unset, Documentation]
        if isinstance(_expected_target_documentation, Unset):
            expected_target_documentation = UNSET
        else:
            expected_target_documentation = Documentation.from_dict(_expected_target_documentation)

        _resolved_documentation = d.pop("resolvedDocumentation", UNSET)
        resolved_documentation: Union[Unset, Documentation]
        if isinstance(_resolved_documentation, Unset):
            resolved_documentation = UNSET
        else:
            resolved_documentation = Documentation.from_dict(_resolved_documentation)

        metadata = []
        _metadata = d.pop("metadata", UNSET)
        for metadata_item_data in _metadata or []:
            metadata_item = ContentMetadata.from_dict(metadata_item_data)

            metadata.append(metadata_item)

        merge_key_behavior = cls(
            key=key,
            merge_behavior=merge_behavior,
            expected_target_content=expected_target_content,
            resolved_content=resolved_content,
            expected_target_documentation=expected_target_documentation,
            resolved_documentation=resolved_documentation,
            metadata=metadata,
        )

        merge_key_behavior.additional_properties = d
        return merge_key_behavior

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
