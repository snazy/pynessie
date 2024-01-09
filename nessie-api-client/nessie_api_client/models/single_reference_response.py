from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.branch import Branch
    from ..models.detached_commit_hash import DetachedCommitHash
    from ..models.tag import Tag


T = TypeVar("T", bound="SingleReferenceResponse")


@_attrs_define
class SingleReferenceResponse:
    """
    Attributes:
        reference (Union['Branch', 'DetachedCommitHash', 'Tag']):
    """

    reference: Union["Branch", "DetachedCommitHash", "Tag"]
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.branch import Branch
        from ..models.tag import Tag

        reference: Dict[str, Any]

        if isinstance(self.reference, Branch):
            reference = self.reference.to_dict()

        elif isinstance(self.reference, Tag):
            reference = self.reference.to_dict()

        else:
            reference = self.reference.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "reference": reference,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.branch import Branch
        from ..models.detached_commit_hash import DetachedCommitHash
        from ..models.tag import Tag

        d = src_dict.copy()

        def _parse_reference(data: object) -> Union["Branch", "DetachedCommitHash", "Tag"]:
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

        reference = _parse_reference(d.pop("reference"))

        single_reference_response = cls(
            reference=reference,
        )

        single_reference_response.additional_properties = d
        return single_reference_response

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
