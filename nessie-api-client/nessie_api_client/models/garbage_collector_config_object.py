from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.references_cutoff_policy import ReferencesCutoffPolicy


T = TypeVar("T", bound="GarbageCollectorConfigObject")


@_attrs_define
class GarbageCollectorConfigObject:
    """
    Attributes:
        default_cutoff_policy (Union[Unset, str]): The default cutoff policy.
            Policies can be one of: - number of commits as an integer value - a duration (see java.time.Duration) - an ISO
            instant - 'NONE', means everything's considered as live
        per_ref_cutoff_policies (Union[Unset, List['ReferencesCutoffPolicy']]):
        new_files_grace_period (Union[Unset, str]): Files that have been created after 'gc-start-time - new-files-grace-
            period' are not being deleted. Example: P1D.
        expected_file_count_per_content (Union[Unset, int]):
    """

    default_cutoff_policy: Union[Unset, str] = UNSET
    per_ref_cutoff_policies: Union[Unset, List["ReferencesCutoffPolicy"]] = UNSET
    new_files_grace_period: Union[Unset, str] = UNSET
    expected_file_count_per_content: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        default_cutoff_policy = self.default_cutoff_policy
        per_ref_cutoff_policies: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.per_ref_cutoff_policies, Unset):
            per_ref_cutoff_policies = []
            for per_ref_cutoff_policies_item_data in self.per_ref_cutoff_policies:
                per_ref_cutoff_policies_item = per_ref_cutoff_policies_item_data.to_dict()

                per_ref_cutoff_policies.append(per_ref_cutoff_policies_item)

        new_files_grace_period = self.new_files_grace_period
        expected_file_count_per_content = self.expected_file_count_per_content

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if default_cutoff_policy is not UNSET:
            field_dict["defaultCutoffPolicy"] = default_cutoff_policy
        if per_ref_cutoff_policies is not UNSET:
            field_dict["perRefCutoffPolicies"] = per_ref_cutoff_policies
        if new_files_grace_period is not UNSET:
            field_dict["newFilesGracePeriod"] = new_files_grace_period
        if expected_file_count_per_content is not UNSET:
            field_dict["expectedFileCountPerContent"] = expected_file_count_per_content

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.references_cutoff_policy import ReferencesCutoffPolicy

        d = src_dict.copy()
        default_cutoff_policy = d.pop("defaultCutoffPolicy", UNSET)

        per_ref_cutoff_policies = []
        _per_ref_cutoff_policies = d.pop("perRefCutoffPolicies", UNSET)
        for per_ref_cutoff_policies_item_data in _per_ref_cutoff_policies or []:
            per_ref_cutoff_policies_item = ReferencesCutoffPolicy.from_dict(per_ref_cutoff_policies_item_data)

            per_ref_cutoff_policies.append(per_ref_cutoff_policies_item)

        new_files_grace_period = d.pop("newFilesGracePeriod", UNSET)

        expected_file_count_per_content = d.pop("expectedFileCountPerContent", UNSET)

        garbage_collector_config_object = cls(
            default_cutoff_policy=default_cutoff_policy,
            per_ref_cutoff_policies=per_ref_cutoff_policies,
            new_files_grace_period=new_files_grace_period,
            expected_file_count_per_content=expected_file_count_per_content,
        )

        garbage_collector_config_object.additional_properties = d
        return garbage_collector_config_object

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
