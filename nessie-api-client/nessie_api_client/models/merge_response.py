from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.merge_per_content_key_details import MergePerContentKeyDetails


T = TypeVar("T", bound="MergeResponse")


@_attrs_define
class MergeResponse:
    """
    Attributes:
        resultant_target_hash (Union[Unset, str]):
        common_ancestor (Union[Unset, str]):
        target_branch (Union[Unset, str]):
        effective_target_hash (Union[Unset, str]):
        expected_hash (Union[Unset, str]):
        details (Union[Unset, List['MergePerContentKeyDetails']]):
    """

    resultant_target_hash: Union[Unset, str] = UNSET
    common_ancestor: Union[Unset, str] = UNSET
    target_branch: Union[Unset, str] = UNSET
    effective_target_hash: Union[Unset, str] = UNSET
    expected_hash: Union[Unset, str] = UNSET
    details: Union[Unset, List["MergePerContentKeyDetails"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        resultant_target_hash = self.resultant_target_hash
        common_ancestor = self.common_ancestor
        target_branch = self.target_branch
        effective_target_hash = self.effective_target_hash
        expected_hash = self.expected_hash
        details: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.details, Unset):
            details = []
            for details_item_data in self.details:
                details_item = details_item_data.to_dict()

                details.append(details_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if resultant_target_hash is not UNSET:
            field_dict["resultantTargetHash"] = resultant_target_hash
        if common_ancestor is not UNSET:
            field_dict["commonAncestor"] = common_ancestor
        if target_branch is not UNSET:
            field_dict["targetBranch"] = target_branch
        if effective_target_hash is not UNSET:
            field_dict["effectiveTargetHash"] = effective_target_hash
        if expected_hash is not UNSET:
            field_dict["expectedHash"] = expected_hash
        if details is not UNSET:
            field_dict["details"] = details

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.merge_per_content_key_details import MergePerContentKeyDetails

        d = src_dict.copy()
        resultant_target_hash = d.pop("resultantTargetHash", UNSET)

        common_ancestor = d.pop("commonAncestor", UNSET)

        target_branch = d.pop("targetBranch", UNSET)

        effective_target_hash = d.pop("effectiveTargetHash", UNSET)

        expected_hash = d.pop("expectedHash", UNSET)

        details = []
        _details = d.pop("details", UNSET)
        for details_item_data in _details or []:
            details_item = MergePerContentKeyDetails.from_dict(details_item_data)

            details.append(details_item)

        merge_response = cls(
            resultant_target_hash=resultant_target_hash,
            common_ancestor=common_ancestor,
            target_branch=target_branch,
            effective_target_hash=effective_target_hash,
            expected_hash=expected_hash,
            details=details,
        )

        merge_response.additional_properties = d
        return merge_response

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
