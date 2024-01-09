from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.content_key import ContentKey
    from ..models.content_type_5 import ContentType5
    from ..models.delta_lake_table import DeltaLakeTable
    from ..models.documentation import Documentation
    from ..models.iceberg_table_state import IcebergTableState
    from ..models.iceberg_view import IcebergView
    from ..models.namespace import Namespace
    from ..models.udf import UDF


T = TypeVar("T", bound="ContentWithKey")


@_attrs_define
class ContentWithKey:
    """
    Attributes:
        key (ContentKey):
        content (Union['ContentType5', 'DeltaLakeTable', 'IcebergTableState', 'IcebergView', 'Namespace', 'UDF']):
        documentation (Union[Unset, Documentation]):
    """

    key: "ContentKey"
    content: Union["ContentType5", "DeltaLakeTable", "IcebergTableState", "IcebergView", "Namespace", "UDF"]
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
        if documentation is not UNSET:
            field_dict["documentation"] = documentation

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.content_key import ContentKey
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

        _documentation = d.pop("documentation", UNSET)
        documentation: Union[Unset, Documentation]
        if isinstance(_documentation, Unset):
            documentation = UNSET
        else:
            documentation = Documentation.from_dict(_documentation)

        content_with_key = cls(
            key=key,
            content=content,
            documentation=documentation,
        )

        content_with_key.additional_properties = d
        return content_with_key

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
