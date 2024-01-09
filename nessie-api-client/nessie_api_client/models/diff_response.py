from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.branch import Branch
    from ..models.detached_commit_hash import DetachedCommitHash
    from ..models.diff_entry import DiffEntry
    from ..models.tag import Tag


T = TypeVar("T", bound="DiffResponse")


@_attrs_define
class DiffResponse:
    """
    Attributes:
        has_more (Union[Unset, bool]):
        token (Union[Unset, str]):
        diffs (Union[Unset, List['DiffEntry']]):
        effective_from_reference (Union['Branch', 'DetachedCommitHash', 'Tag', Unset]):
        effective_to_reference (Union['Branch', 'DetachedCommitHash', 'Tag', Unset]):
    """

    has_more: Union[Unset, bool] = UNSET
    token: Union[Unset, str] = UNSET
    diffs: Union[Unset, List["DiffEntry"]] = UNSET
    effective_from_reference: Union["Branch", "DetachedCommitHash", "Tag", Unset] = UNSET
    effective_to_reference: Union["Branch", "DetachedCommitHash", "Tag", Unset] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.branch import Branch
        from ..models.tag import Tag

        has_more = self.has_more
        token = self.token
        diffs: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.diffs, Unset):
            diffs = []
            for diffs_item_data in self.diffs:
                diffs_item = diffs_item_data.to_dict()

                diffs.append(diffs_item)

        effective_from_reference: Union[Dict[str, Any], Unset]
        if isinstance(self.effective_from_reference, Unset):
            effective_from_reference = UNSET

        elif isinstance(self.effective_from_reference, Branch):
            effective_from_reference = self.effective_from_reference.to_dict()

        elif isinstance(self.effective_from_reference, Tag):
            effective_from_reference = self.effective_from_reference.to_dict()

        else:
            effective_from_reference = self.effective_from_reference.to_dict()

        effective_to_reference: Union[Dict[str, Any], Unset]
        if isinstance(self.effective_to_reference, Unset):
            effective_to_reference = UNSET

        elif isinstance(self.effective_to_reference, Branch):
            effective_to_reference = self.effective_to_reference.to_dict()

        elif isinstance(self.effective_to_reference, Tag):
            effective_to_reference = self.effective_to_reference.to_dict()

        else:
            effective_to_reference = self.effective_to_reference.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if has_more is not UNSET:
            field_dict["hasMore"] = has_more
        if token is not UNSET:
            field_dict["token"] = token
        if diffs is not UNSET:
            field_dict["diffs"] = diffs
        if effective_from_reference is not UNSET:
            field_dict["effectiveFromReference"] = effective_from_reference
        if effective_to_reference is not UNSET:
            field_dict["effectiveToReference"] = effective_to_reference

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.branch import Branch
        from ..models.detached_commit_hash import DetachedCommitHash
        from ..models.diff_entry import DiffEntry
        from ..models.tag import Tag

        d = src_dict.copy()
        has_more = d.pop("hasMore", UNSET)

        token = d.pop("token", UNSET)

        diffs = []
        _diffs = d.pop("diffs", UNSET)
        for diffs_item_data in _diffs or []:
            diffs_item = DiffEntry.from_dict(diffs_item_data)

            diffs.append(diffs_item)

        def _parse_effective_from_reference(data: object) -> Union["Branch", "DetachedCommitHash", "Tag", Unset]:
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

        effective_from_reference = _parse_effective_from_reference(d.pop("effectiveFromReference", UNSET))

        def _parse_effective_to_reference(data: object) -> Union["Branch", "DetachedCommitHash", "Tag", Unset]:
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

        effective_to_reference = _parse_effective_to_reference(d.pop("effectiveToReference", UNSET))

        diff_response = cls(
            has_more=has_more,
            token=token,
            diffs=diffs,
            effective_from_reference=effective_from_reference,
            effective_to_reference=effective_to_reference,
        )

        diff_response.additional_properties = d
        return diff_response

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
