from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.merge_behavior import MergeBehavior
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.conflict import Conflict
    from ..models.content_key import ContentKey


T = TypeVar("T", bound="MergePerContentKeyDetails")


@_attrs_define
class MergePerContentKeyDetails:
    """
    Attributes:
        key (Union[Unset, ContentKey]):
        merge_behavior (Union[Unset, MergeBehavior]):
        conflict (Union[Unset, Conflict]):
    """

    key: Union[Unset, "ContentKey"] = UNSET
    merge_behavior: Union[Unset, MergeBehavior] = UNSET
    conflict: Union[Unset, "Conflict"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        key: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.key, Unset):
            key = self.key.to_dict()

        merge_behavior: Union[Unset, str] = UNSET
        if not isinstance(self.merge_behavior, Unset):
            merge_behavior = self.merge_behavior.value

        conflict: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.conflict, Unset):
            conflict = self.conflict.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if key is not UNSET:
            field_dict["key"] = key
        if merge_behavior is not UNSET:
            field_dict["mergeBehavior"] = merge_behavior
        if conflict is not UNSET:
            field_dict["conflict"] = conflict

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.conflict import Conflict
        from ..models.content_key import ContentKey

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

        _conflict = d.pop("conflict", UNSET)
        conflict: Union[Unset, Conflict]
        if isinstance(_conflict, Unset):
            conflict = UNSET
        else:
            conflict = Conflict.from_dict(_conflict)

        merge_per_content_key_details = cls(
            key=key,
            merge_behavior=merge_behavior,
            conflict=conflict,
        )

        merge_per_content_key_details.additional_properties = d
        return merge_per_content_key_details

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
