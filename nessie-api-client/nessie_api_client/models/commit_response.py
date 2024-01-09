from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.added_content import AddedContent
    from ..models.branch import Branch


T = TypeVar("T", bound="CommitResponse")


@_attrs_define
class CommitResponse:
    """
    Attributes:
        target_branch (Branch):
        added_contents (Union[Unset, List['AddedContent']]):
    """

    target_branch: "Branch"
    added_contents: Union[Unset, List["AddedContent"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        target_branch = self.target_branch.to_dict()

        added_contents: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.added_contents, Unset):
            added_contents = []
            for added_contents_item_data in self.added_contents:
                added_contents_item = added_contents_item_data.to_dict()

                added_contents.append(added_contents_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "targetBranch": target_branch,
            }
        )
        if added_contents is not UNSET:
            field_dict["addedContents"] = added_contents

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.added_content import AddedContent
        from ..models.branch import Branch

        d = src_dict.copy()
        target_branch = Branch.from_dict(d.pop("targetBranch"))

        added_contents = []
        _added_contents = d.pop("addedContents", UNSET)
        for added_contents_item_data in _added_contents or []:
            added_contents_item = AddedContent.from_dict(added_contents_item_data)

            added_contents.append(added_contents_item)

        commit_response = cls(
            target_branch=target_branch,
            added_contents=added_contents,
        )

        commit_response.additional_properties = d
        return commit_response

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
