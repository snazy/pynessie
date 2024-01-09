from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.branch import Branch
    from ..models.content_with_key import ContentWithKey
    from ..models.detached_commit_hash import DetachedCommitHash
    from ..models.tag import Tag


T = TypeVar("T", bound="GetMultipleContentsResponse")


@_attrs_define
class GetMultipleContentsResponse:
    """
    Attributes:
        contents (List['ContentWithKey']):
        effective_reference (Union['Branch', 'DetachedCommitHash', 'Tag', Unset]):
    """

    contents: List["ContentWithKey"]
    effective_reference: Union["Branch", "DetachedCommitHash", "Tag", Unset] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.branch import Branch
        from ..models.tag import Tag

        contents = []
        for contents_item_data in self.contents:
            contents_item = contents_item_data.to_dict()

            contents.append(contents_item)

        effective_reference: Union[Dict[str, Any], Unset]
        if isinstance(self.effective_reference, Unset):
            effective_reference = UNSET

        elif isinstance(self.effective_reference, Branch):
            effective_reference = self.effective_reference.to_dict()

        elif isinstance(self.effective_reference, Tag):
            effective_reference = self.effective_reference.to_dict()

        else:
            effective_reference = self.effective_reference.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "contents": contents,
            }
        )
        if effective_reference is not UNSET:
            field_dict["effectiveReference"] = effective_reference

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.branch import Branch
        from ..models.content_with_key import ContentWithKey
        from ..models.detached_commit_hash import DetachedCommitHash
        from ..models.tag import Tag

        d = src_dict.copy()
        contents = []
        _contents = d.pop("contents")
        for contents_item_data in _contents:
            contents_item = ContentWithKey.from_dict(contents_item_data)

            contents.append(contents_item)

        def _parse_effective_reference(data: object) -> Union["Branch", "DetachedCommitHash", "Tag", Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_reference_type_0 = Branch.from_dict(data)

                return componentsschemas_reference_type_0
            except:  # noqa: E722
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_reference_type_1 = Tag.from_dict(data)

                return componentsschemas_reference_type_1
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_reference_type_2 = DetachedCommitHash.from_dict(data)

            return componentsschemas_reference_type_2

        effective_reference = _parse_effective_reference(d.pop("effectiveReference", UNSET))

        get_multiple_contents_response = cls(
            contents=contents,
            effective_reference=effective_reference,
        )

        get_multiple_contents_response.additional_properties = d
        return get_multiple_contents_response

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
