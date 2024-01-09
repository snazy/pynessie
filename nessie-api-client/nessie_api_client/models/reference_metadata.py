from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.commit_meta import CommitMeta


T = TypeVar("T", bound="ReferenceMetadata")


@_attrs_define
class ReferenceMetadata:
    """Only returned by the server when explicitly requested by the client and contains the following information:

    - numCommitsAhead (number of commits ahead of the default branch)

    - numCommitsBehind (number of commits behind the default branch)

    - commitMetaOfHEAD (the commit metadata of the HEAD commit)

    - commonAncestorHash (the hash of the common ancestor in relation to the default branch).

    - numTotalCommits (the total number of commits in this reference).


        Attributes:
            num_commits_ahead (Union[Unset, int]):
            num_commits_behind (Union[Unset, int]):
            commit_meta_of_head (Union[Unset, CommitMeta]):
            common_ancestor_hash (Union[Unset, str]):
            num_total_commits (Union[Unset, int]):
    """

    num_commits_ahead: Union[Unset, int] = UNSET
    num_commits_behind: Union[Unset, int] = UNSET
    commit_meta_of_head: Union[Unset, "CommitMeta"] = UNSET
    common_ancestor_hash: Union[Unset, str] = UNSET
    num_total_commits: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        num_commits_ahead = self.num_commits_ahead
        num_commits_behind = self.num_commits_behind
        commit_meta_of_head: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.commit_meta_of_head, Unset):
            commit_meta_of_head = self.commit_meta_of_head.to_dict()

        common_ancestor_hash = self.common_ancestor_hash
        num_total_commits = self.num_total_commits

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if num_commits_ahead is not UNSET:
            field_dict["numCommitsAhead"] = num_commits_ahead
        if num_commits_behind is not UNSET:
            field_dict["numCommitsBehind"] = num_commits_behind
        if commit_meta_of_head is not UNSET:
            field_dict["commitMetaOfHEAD"] = commit_meta_of_head
        if common_ancestor_hash is not UNSET:
            field_dict["commonAncestorHash"] = common_ancestor_hash
        if num_total_commits is not UNSET:
            field_dict["numTotalCommits"] = num_total_commits

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.commit_meta import CommitMeta

        d = src_dict.copy()
        num_commits_ahead = d.pop("numCommitsAhead", UNSET)

        num_commits_behind = d.pop("numCommitsBehind", UNSET)

        _commit_meta_of_head = d.pop("commitMetaOfHEAD", UNSET)
        commit_meta_of_head: Union[Unset, CommitMeta]
        if isinstance(_commit_meta_of_head, Unset):
            commit_meta_of_head = UNSET
        else:
            commit_meta_of_head = CommitMeta.from_dict(_commit_meta_of_head)

        common_ancestor_hash = d.pop("commonAncestorHash", UNSET)

        num_total_commits = d.pop("numTotalCommits", UNSET)

        reference_metadata = cls(
            num_commits_ahead=num_commits_ahead,
            num_commits_behind=num_commits_behind,
            commit_meta_of_head=commit_meta_of_head,
            common_ancestor_hash=common_ancestor_hash,
            num_total_commits=num_total_commits,
        )

        reference_metadata.additional_properties = d
        return reference_metadata

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
