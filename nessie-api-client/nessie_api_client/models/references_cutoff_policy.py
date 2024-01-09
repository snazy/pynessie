from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ReferencesCutoffPolicy")


@_attrs_define
class ReferencesCutoffPolicy:
    """Cutoff policies per reference names. Supplied as a ref-name-pattern=policy tuple. Reference name patterns are
    regular expressions.

        Attributes:
            reference_name_pattern (Union[Unset, str]): Reference name patterns as a regular expressions.
            policy (Union[Unset, str]): Policies can be one of: - number of commits as an integer value - a duration (see
                java.time.Duration) - an ISO instant - 'NONE', means everything's considered as live
    """

    reference_name_pattern: Union[Unset, str] = UNSET
    policy: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        reference_name_pattern = self.reference_name_pattern
        policy = self.policy

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if reference_name_pattern is not UNSET:
            field_dict["referenceNamePattern"] = reference_name_pattern
        if policy is not UNSET:
            field_dict["policy"] = policy

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        reference_name_pattern = d.pop("referenceNamePattern", UNSET)

        policy = d.pop("policy", UNSET)

        references_cutoff_policy = cls(
            reference_name_pattern=reference_name_pattern,
            policy=policy,
        )

        references_cutoff_policy.additional_properties = d
        return references_cutoff_policy

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
