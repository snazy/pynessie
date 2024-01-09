from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.merge_behavior import MergeBehavior
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.merge_key_behavior import MergeKeyBehavior


T = TypeVar("T", bound="Transplant")


@_attrs_define
class Transplant:
    """
    Attributes:
        from_ref_name (str):
        hashes_to_transplant (List[str]):
        key_merge_modes (Union[Unset, List['MergeKeyBehavior']]):
        default_key_merge_mode (Union[Unset, MergeBehavior]):
        dry_run (Union[Unset, bool]):
        fetch_additional_info (Union[Unset, bool]):
        return_conflict_as_result (Union[Unset, bool]):
    """

    from_ref_name: str
    hashes_to_transplant: List[str]
    key_merge_modes: Union[Unset, List["MergeKeyBehavior"]] = UNSET
    default_key_merge_mode: Union[Unset, MergeBehavior] = UNSET
    dry_run: Union[Unset, bool] = UNSET
    fetch_additional_info: Union[Unset, bool] = UNSET
    return_conflict_as_result: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from_ref_name = self.from_ref_name
        hashes_to_transplant = self.hashes_to_transplant

        key_merge_modes: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.key_merge_modes, Unset):
            key_merge_modes = []
            for key_merge_modes_item_data in self.key_merge_modes:
                key_merge_modes_item = key_merge_modes_item_data.to_dict()

                key_merge_modes.append(key_merge_modes_item)

        default_key_merge_mode: Union[Unset, str] = UNSET
        if not isinstance(self.default_key_merge_mode, Unset):
            default_key_merge_mode = self.default_key_merge_mode.value

        dry_run = self.dry_run
        fetch_additional_info = self.fetch_additional_info
        return_conflict_as_result = self.return_conflict_as_result

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "fromRefName": from_ref_name,
                "hashesToTransplant": hashes_to_transplant,
            }
        )
        if key_merge_modes is not UNSET:
            field_dict["keyMergeModes"] = key_merge_modes
        if default_key_merge_mode is not UNSET:
            field_dict["defaultKeyMergeMode"] = default_key_merge_mode
        if dry_run is not UNSET:
            field_dict["dryRun"] = dry_run
        if fetch_additional_info is not UNSET:
            field_dict["fetchAdditionalInfo"] = fetch_additional_info
        if return_conflict_as_result is not UNSET:
            field_dict["returnConflictAsResult"] = return_conflict_as_result

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.merge_key_behavior import MergeKeyBehavior

        d = src_dict.copy()
        from_ref_name = d.pop("fromRefName")

        hashes_to_transplant = cast(List[str], d.pop("hashesToTransplant"))

        key_merge_modes = []
        _key_merge_modes = d.pop("keyMergeModes", UNSET)
        for key_merge_modes_item_data in _key_merge_modes or []:
            key_merge_modes_item = MergeKeyBehavior.from_dict(key_merge_modes_item_data)

            key_merge_modes.append(key_merge_modes_item)

        _default_key_merge_mode = d.pop("defaultKeyMergeMode", UNSET)
        default_key_merge_mode: Union[Unset, MergeBehavior]
        if isinstance(_default_key_merge_mode, Unset):
            default_key_merge_mode = UNSET
        else:
            default_key_merge_mode = MergeBehavior(_default_key_merge_mode)

        dry_run = d.pop("dryRun", UNSET)

        fetch_additional_info = d.pop("fetchAdditionalInfo", UNSET)

        return_conflict_as_result = d.pop("returnConflictAsResult", UNSET)

        transplant = cls(
            from_ref_name=from_ref_name,
            hashes_to_transplant=hashes_to_transplant,
            key_merge_modes=key_merge_modes,
            default_key_merge_mode=default_key_merge_mode,
            dry_run=dry_run,
            fetch_additional_info=fetch_additional_info,
            return_conflict_as_result=return_conflict_as_result,
        )

        transplant.additional_properties = d
        return transplant

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
