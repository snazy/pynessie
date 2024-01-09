from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.reference_metadata import ReferenceMetadata


T = TypeVar("T", bound="DetachedCommitHash")


@_attrs_define
class DetachedCommitHash:
    """
    Attributes:
        hash_ (str):
        metadata (Union[Unset, ReferenceMetadata]): Only returned by the server when explicitly requested by the client
            and contains the following information:

            - numCommitsAhead (number of commits ahead of the default branch)

            - numCommitsBehind (number of commits behind the default branch)

            - commitMetaOfHEAD (the commit metadata of the HEAD commit)

            - commonAncestorHash (the hash of the common ancestor in relation to the default branch).

            - numTotalCommits (the total number of commits in this reference).

    """

    hash_: str
    metadata: Union[Unset, "ReferenceMetadata"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        hash_ = self.hash_
        metadata: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "hash": hash_,
            }
        )
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.reference_metadata import ReferenceMetadata

        d = src_dict.copy()
        hash_ = d.pop("hash")

        _metadata = d.pop("metadata", UNSET)
        metadata: Union[Unset, ReferenceMetadata]
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = ReferenceMetadata.from_dict(_metadata)

        detached_commit_hash = cls(
            hash_=hash_,
            metadata=metadata,
        )

        detached_commit_hash.additional_properties = d
        return detached_commit_hash

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
