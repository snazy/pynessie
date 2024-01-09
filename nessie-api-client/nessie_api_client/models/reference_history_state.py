from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.commit_consistency import CommitConsistency
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.commit_meta import CommitMeta


T = TypeVar("T", bound="ReferenceHistoryState")


@_attrs_define
class ReferenceHistoryState:
    """Describes the consistency status of a commit within a `ReferenceHistoryResponse` object.

    Possible values of the `CommitConsistency` enum:
    - `NOT_CHECKED` means: Consistency was not checked.
    - `COMMIT_CONSISTENT` means: The commit object, its index information and all reachable content is present.
    - `COMMIT_CONTENT_INCONSISTENT` means: The commit object is present and its index is accessible, but some content
    reachable from the commit is not present.
    - `COMMIT_INCONSISTENT` means: The commit is inconsistent in a way that makes it impossible to access the commit,
    for example if the commit object itself or its index information is missing.

        Attributes:
            commit_hash (Union[Unset, str]): Nessie commit ID.
            commit_consistency (Union[Unset, CommitConsistency]):
            meta (Union[Unset, CommitMeta]):
    """

    commit_hash: Union[Unset, str] = UNSET
    commit_consistency: Union[Unset, CommitConsistency] = UNSET
    meta: Union[Unset, "CommitMeta"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        commit_hash = self.commit_hash
        commit_consistency: Union[Unset, str] = UNSET
        if not isinstance(self.commit_consistency, Unset):
            commit_consistency = self.commit_consistency.value

        meta: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.meta, Unset):
            meta = self.meta.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if commit_hash is not UNSET:
            field_dict["commitHash"] = commit_hash
        if commit_consistency is not UNSET:
            field_dict["commitConsistency"] = commit_consistency
        if meta is not UNSET:
            field_dict["meta"] = meta

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.commit_meta import CommitMeta

        d = src_dict.copy()
        commit_hash = d.pop("commitHash", UNSET)

        _commit_consistency = d.pop("commitConsistency", UNSET)
        commit_consistency: Union[Unset, CommitConsistency]
        if isinstance(_commit_consistency, Unset):
            commit_consistency = UNSET
        else:
            commit_consistency = CommitConsistency(_commit_consistency)

        _meta = d.pop("meta", UNSET)
        meta: Union[Unset, CommitMeta]
        if isinstance(_meta, Unset):
            meta = UNSET
        else:
            meta = CommitMeta.from_dict(_meta)

        reference_history_state = cls(
            commit_hash=commit_hash,
            commit_consistency=commit_consistency,
            meta=meta,
        )

        reference_history_state.additional_properties = d
        return reference_history_state

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
