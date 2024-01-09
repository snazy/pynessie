from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.content_key import ContentKey
    from ..models.content_type_5 import ContentType5
    from ..models.delta_lake_table import DeltaLakeTable
    from ..models.iceberg_table_state import IcebergTableState
    from ..models.iceberg_view import IcebergView
    from ..models.namespace import Namespace
    from ..models.udf import UDF


T = TypeVar("T", bound="DiffEntry")


@_attrs_define
class DiffEntry:
    """
    Attributes:
        key (Union[Unset, ContentKey]):
        from_ (Union['ContentType5', 'DeltaLakeTable', 'IcebergTableState', 'IcebergView', 'Namespace', 'UDF', Unset]):
        to (Union['ContentType5', 'DeltaLakeTable', 'IcebergTableState', 'IcebergView', 'Namespace', 'UDF', Unset]):
    """

    key: Union[Unset, "ContentKey"] = UNSET
    from_: Union[
        "ContentType5", "DeltaLakeTable", "IcebergTableState", "IcebergView", "Namespace", "UDF", Unset
    ] = UNSET
    to: Union["ContentType5", "DeltaLakeTable", "IcebergTableState", "IcebergView", "Namespace", "UDF", Unset] = UNSET
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

        from_: Union[Dict[str, Any], Unset]
        if isinstance(self.from_, Unset):
            from_ = UNSET

        elif isinstance(self.from_, IcebergTableState):
            from_ = self.from_.to_dict()

        elif isinstance(self.from_, DeltaLakeTable):
            from_ = self.from_.to_dict()

        elif isinstance(self.from_, IcebergView):
            from_ = self.from_.to_dict()

        elif isinstance(self.from_, Namespace):
            from_ = self.from_.to_dict()

        elif isinstance(self.from_, UDF):
            from_ = self.from_.to_dict()

        else:
            from_ = self.from_.to_dict()

        to: Union[Dict[str, Any], Unset]
        if isinstance(self.to, Unset):
            to = UNSET

        elif isinstance(self.to, IcebergTableState):
            to = self.to.to_dict()

        elif isinstance(self.to, DeltaLakeTable):
            to = self.to.to_dict()

        elif isinstance(self.to, IcebergView):
            to = self.to.to_dict()

        elif isinstance(self.to, Namespace):
            to = self.to.to_dict()

        elif isinstance(self.to, UDF):
            to = self.to.to_dict()

        else:
            to = self.to.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if key is not UNSET:
            field_dict["key"] = key
        if from_ is not UNSET:
            field_dict["from"] = from_
        if to is not UNSET:
            field_dict["to"] = to

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.content_key import ContentKey
        from ..models.content_type_5 import ContentType5
        from ..models.delta_lake_table import DeltaLakeTable
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

        def _parse_from_(
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

        from_ = _parse_from_(d.pop("from", UNSET))

        def _parse_to(
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

        to = _parse_to(d.pop("to", UNSET))

        diff_entry = cls(
            key=key,
            from_=from_,
            to=to,
        )

        diff_entry.additional_properties = d
        return diff_entry

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
