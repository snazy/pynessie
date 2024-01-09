import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.commit_meta_all_properties import CommitMetaAllProperties
    from ..models.commit_meta_properties import CommitMetaProperties


T = TypeVar("T", bound="CommitMeta")


@_attrs_define
class CommitMeta:
    """
    Attributes:
        authors (List[str]):
        all_signed_off_by (List[str]):
        message (str):
        properties (CommitMetaProperties):
        all_properties (CommitMetaAllProperties):
        parent_commit_hashes (List[str]):
        hash_ (Union[Unset, str]):
        committer (Union[Unset, str]):
        author (Union[Unset, str]):
        signed_off_by (Union[Unset, str]):
        commit_time (Union[Unset, datetime.datetime]):  Example: 2022-03-10T16:15:50Z.
        author_time (Union[Unset, datetime.datetime]):  Example: 2022-03-10T16:15:50Z.
    """

    authors: List[str]
    all_signed_off_by: List[str]
    message: str
    properties: "CommitMetaProperties"
    all_properties: "CommitMetaAllProperties"
    parent_commit_hashes: List[str]
    hash_: Union[Unset, str] = UNSET
    committer: Union[Unset, str] = UNSET
    author: Union[Unset, str] = UNSET
    signed_off_by: Union[Unset, str] = UNSET
    commit_time: Union[Unset, datetime.datetime] = UNSET
    author_time: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        authors = self.authors

        all_signed_off_by = self.all_signed_off_by

        message = self.message
        properties = self.properties.to_dict()

        all_properties = self.all_properties.to_dict()

        parent_commit_hashes = self.parent_commit_hashes

        hash_ = self.hash_
        committer = self.committer
        author = self.author
        signed_off_by = self.signed_off_by
        commit_time: Union[Unset, str] = UNSET
        if not isinstance(self.commit_time, Unset):
            commit_time = self.commit_time.isoformat()

        author_time: Union[Unset, str] = UNSET
        if not isinstance(self.author_time, Unset):
            author_time = self.author_time.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "authors": authors,
                "allSignedOffBy": all_signed_off_by,
                "message": message,
                "properties": properties,
                "allProperties": all_properties,
                "parentCommitHashes": parent_commit_hashes,
            }
        )
        if hash_ is not UNSET:
            field_dict["hash"] = hash_
        if committer is not UNSET:
            field_dict["committer"] = committer
        if author is not UNSET:
            field_dict["author"] = author
        if signed_off_by is not UNSET:
            field_dict["signedOffBy"] = signed_off_by
        if commit_time is not UNSET:
            field_dict["commitTime"] = commit_time
        if author_time is not UNSET:
            field_dict["authorTime"] = author_time

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.commit_meta_all_properties import CommitMetaAllProperties
        from ..models.commit_meta_properties import CommitMetaProperties

        d = src_dict.copy()
        authors = cast(List[str], d.pop("authors"))

        all_signed_off_by = cast(List[str], d.pop("allSignedOffBy"))

        message = d.pop("message")

        properties = CommitMetaProperties.from_dict(d.pop("properties"))

        all_properties = CommitMetaAllProperties.from_dict(d.pop("allProperties"))

        parent_commit_hashes = cast(List[str], d.pop("parentCommitHashes"))

        hash_ = d.pop("hash", UNSET)

        committer = d.pop("committer", UNSET)

        author = d.pop("author", UNSET)

        signed_off_by = d.pop("signedOffBy", UNSET)

        _commit_time = d.pop("commitTime", UNSET)
        commit_time: Union[Unset, datetime.datetime]
        if isinstance(_commit_time, Unset):
            commit_time = UNSET
        else:
            commit_time = isoparse(_commit_time)

        _author_time = d.pop("authorTime", UNSET)
        author_time: Union[Unset, datetime.datetime]
        if isinstance(_author_time, Unset):
            author_time = UNSET
        else:
            author_time = isoparse(_author_time)

        commit_meta = cls(
            authors=authors,
            all_signed_off_by=all_signed_off_by,
            message=message,
            properties=properties,
            all_properties=all_properties,
            parent_commit_hashes=parent_commit_hashes,
            hash_=hash_,
            committer=committer,
            author=author,
            signed_off_by=signed_off_by,
            commit_time=commit_time,
            author_time=author_time,
        )

        commit_meta.additional_properties = d
        return commit_meta

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
