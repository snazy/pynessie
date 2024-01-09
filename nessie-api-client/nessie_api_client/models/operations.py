from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.commit_meta import CommitMeta
    from ..models.delete_content_operation_for_a_content_key import DeleteContentOperationForAContentKey
    from ..models.put_content_operation_for_a_content_key import PutContentOperationForAContentKey
    from ..models.unchanged import Unchanged


T = TypeVar("T", bound="Operations")


@_attrs_define
class Operations:
    """
    Attributes:
        commit_meta (CommitMeta):
        operations (List[Union['DeleteContentOperationForAContentKey', 'PutContentOperationForAContentKey',
            'Unchanged']]):
    """

    commit_meta: "CommitMeta"
    operations: List[Union["DeleteContentOperationForAContentKey", "PutContentOperationForAContentKey", "Unchanged"]]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.put_content_operation_for_a_content_key import PutContentOperationForAContentKey
        from ..models.unchanged import Unchanged

        commit_meta = self.commit_meta.to_dict()

        operations = []
        for operations_item_data in self.operations:
            operations_item: Dict[str, Any]

            if isinstance(operations_item_data, PutContentOperationForAContentKey):
                operations_item = operations_item_data.to_dict()

            elif isinstance(operations_item_data, Unchanged):
                operations_item = operations_item_data.to_dict()

            else:
                operations_item = operations_item_data.to_dict()

            operations.append(operations_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "commitMeta": commit_meta,
                "operations": operations,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.commit_meta import CommitMeta
        from ..models.delete_content_operation_for_a_content_key import DeleteContentOperationForAContentKey
        from ..models.put_content_operation_for_a_content_key import PutContentOperationForAContentKey
        from ..models.unchanged import Unchanged

        d = src_dict.copy()
        commit_meta = CommitMeta.from_dict(d.pop("commitMeta"))

        operations = []
        _operations = d.pop("operations")
        for operations_item_data in _operations:

            def _parse_operations_item(
                data: object,
            ) -> Union["DeleteContentOperationForAContentKey", "PutContentOperationForAContentKey", "Unchanged"]:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_operation_type_0 = PutContentOperationForAContentKey.from_dict(data)

                    return componentsschemas_operation_type_0
                except:  # noqa: E722
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_operation_type_1 = Unchanged.from_dict(data)

                    return componentsschemas_operation_type_1
                except:  # noqa: E722
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_operation_type_2 = DeleteContentOperationForAContentKey.from_dict(data)

                return componentsschemas_operation_type_2

            operations_item = _parse_operations_item(operations_item_data)

            operations.append(operations_item)

        operations = cls(
            commit_meta=commit_meta,
            operations=operations,
        )

        operations.additional_properties = d
        return operations

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
