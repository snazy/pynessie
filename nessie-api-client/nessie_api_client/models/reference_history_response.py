from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.commit_consistency import CommitConsistency

if TYPE_CHECKING:
    from ..models.branch import Branch
    from ..models.detached_commit_hash import DetachedCommitHash
    from ..models.reference_history_state import ReferenceHistoryState
    from ..models.tag import Tag


T = TypeVar("T", bound="ReferenceHistoryResponse")


@_attrs_define
class ReferenceHistoryResponse:
    """Describes the consistency status of a named reference.

    Possible values of the `CommitConsistency` enum:
    - `NOT_CHECKED` means: Consistency was not checked.
    - `COMMIT_CONSISTENT` means: The commit object, its index information and all reachable content is present.
    - `COMMIT_CONTENT_INCONSISTENT` means: The commit object is present and its index is accessible, but some content
    reachable from the commit is not present.
    - `COMMIT_INCONSISTENT` means: The commit is inconsistent in a way that makes it impossible to access the commit,
    for example if the commit object itself or its index information is missing.

        Attributes:
            reference (Union['Branch', 'DetachedCommitHash', 'Tag']):
            current (ReferenceHistoryState): Describes the consistency status of a commit within a
                `ReferenceHistoryResponse` object.

                Possible values of the `CommitConsistency` enum:
                - `NOT_CHECKED` means: Consistency was not checked.
                - `COMMIT_CONSISTENT` means: The commit object, its index information and all reachable content is present.
                - `COMMIT_CONTENT_INCONSISTENT` means: The commit object is present and its index is accessible, but some
                content reachable from the commit is not present.
                - `COMMIT_INCONSISTENT` means: The commit is inconsistent in a way that makes it impossible to access the
                commit, for example if the commit object itself or its index information is missing.
            previous (List['ReferenceHistoryState']): Consistency status of the recorded recent HEADs of the reference,
                including re-assign operations.
            commit_log_consistency (CommitConsistency):
    """

    reference: Union["Branch", "DetachedCommitHash", "Tag"]
    current: "ReferenceHistoryState"
    previous: List["ReferenceHistoryState"]
    commit_log_consistency: CommitConsistency
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

        current = self.current.to_dict()

        previous = []
        for previous_item_data in self.previous:
            previous_item = previous_item_data.to_dict()

            previous.append(previous_item)

        commit_log_consistency = self.commit_log_consistency.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "reference": reference,
                "current": current,
                "previous": previous,
                "commitLogConsistency": commit_log_consistency,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.branch import Branch
        from ..models.detached_commit_hash import DetachedCommitHash
        from ..models.reference_history_state import ReferenceHistoryState
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

        current = ReferenceHistoryState.from_dict(d.pop("current"))

        previous = []
        _previous = d.pop("previous")
        for previous_item_data in _previous:
            previous_item = ReferenceHistoryState.from_dict(previous_item_data)

            previous.append(previous_item)

        commit_log_consistency = CommitConsistency(d.pop("commitLogConsistency"))

        reference_history_response = cls(
            reference=reference,
            current=current,
            previous=previous,
            commit_log_consistency=commit_log_consistency,
        )

        reference_history_response.additional_properties = d
        return reference_history_response

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
