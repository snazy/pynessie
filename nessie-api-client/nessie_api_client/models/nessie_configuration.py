import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.nessie_configuration_additional_properties import NessieConfigurationAdditionalProperties


T = TypeVar("T", bound="NessieConfiguration")


@_attrs_define
class NessieConfiguration:
    """Configuration object to tell a client how a server is configured.

    Attributes:
        default_branch (Union[Unset, str]):
        min_supported_api_version (Union[Unset, int]):
        max_supported_api_version (Union[Unset, int]):
        actual_api_version (Union[Unset, int]):
        spec_version (Union[Unset, str]): Semver version representing the behavior of the Nessie server.

            Additional functionality might be added to Nessie servers within a "spec major version" in a non-breaking way.
            Clients are encouraged to check the spec version when using such added functionality.
        no_ancestor_hash (Union[Unset, str]):
        repository_creation_timestamp (Union[Unset, datetime.datetime]):  Example: 2022-03-10T16:15:50Z.
        oldest_possible_commit_timestamp (Union[Unset, datetime.datetime]):  Example: 2022-03-10T16:15:50Z.
        additional_properties (Union[Unset, NessieConfigurationAdditionalProperties]):
    """

    default_branch: Union[Unset, str] = UNSET
    min_supported_api_version: Union[Unset, int] = UNSET
    max_supported_api_version: Union[Unset, int] = UNSET
    actual_api_version: Union[Unset, int] = UNSET
    spec_version: Union[Unset, str] = UNSET
    no_ancestor_hash: Union[Unset, str] = UNSET
    repository_creation_timestamp: Union[Unset, datetime.datetime] = UNSET
    oldest_possible_commit_timestamp: Union[Unset, datetime.datetime] = UNSET
    additional_properties: Union[Unset, "NessieConfigurationAdditionalProperties"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        default_branch = self.default_branch
        min_supported_api_version = self.min_supported_api_version
        max_supported_api_version = self.max_supported_api_version
        actual_api_version = self.actual_api_version
        spec_version = self.spec_version
        no_ancestor_hash = self.no_ancestor_hash
        repository_creation_timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.repository_creation_timestamp, Unset):
            repository_creation_timestamp = self.repository_creation_timestamp.isoformat()

        oldest_possible_commit_timestamp: Union[Unset, str] = UNSET
        if not isinstance(self.oldest_possible_commit_timestamp, Unset):
            oldest_possible_commit_timestamp = self.oldest_possible_commit_timestamp.isoformat()

        additional_properties: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.additional_properties, Unset):
            additional_properties = self.additional_properties.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if default_branch is not UNSET:
            field_dict["defaultBranch"] = default_branch
        if min_supported_api_version is not UNSET:
            field_dict["minSupportedApiVersion"] = min_supported_api_version
        if max_supported_api_version is not UNSET:
            field_dict["maxSupportedApiVersion"] = max_supported_api_version
        if actual_api_version is not UNSET:
            field_dict["actualApiVersion"] = actual_api_version
        if spec_version is not UNSET:
            field_dict["specVersion"] = spec_version
        if no_ancestor_hash is not UNSET:
            field_dict["noAncestorHash"] = no_ancestor_hash
        if repository_creation_timestamp is not UNSET:
            field_dict["repositoryCreationTimestamp"] = repository_creation_timestamp
        if oldest_possible_commit_timestamp is not UNSET:
            field_dict["oldestPossibleCommitTimestamp"] = oldest_possible_commit_timestamp
        if additional_properties is not UNSET:
            field_dict["additionalProperties"] = additional_properties

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.nessie_configuration_additional_properties import NessieConfigurationAdditionalProperties

        d = src_dict.copy()
        default_branch = d.pop("defaultBranch", UNSET)

        min_supported_api_version = d.pop("minSupportedApiVersion", UNSET)

        max_supported_api_version = d.pop("maxSupportedApiVersion", UNSET)

        actual_api_version = d.pop("actualApiVersion", UNSET)

        spec_version = d.pop("specVersion", UNSET)

        no_ancestor_hash = d.pop("noAncestorHash", UNSET)

        _repository_creation_timestamp = d.pop("repositoryCreationTimestamp", UNSET)
        repository_creation_timestamp: Union[Unset, datetime.datetime]
        if isinstance(_repository_creation_timestamp, Unset):
            repository_creation_timestamp = UNSET
        else:
            repository_creation_timestamp = isoparse(_repository_creation_timestamp)

        _oldest_possible_commit_timestamp = d.pop("oldestPossibleCommitTimestamp", UNSET)
        oldest_possible_commit_timestamp: Union[Unset, datetime.datetime]
        if isinstance(_oldest_possible_commit_timestamp, Unset):
            oldest_possible_commit_timestamp = UNSET
        else:
            oldest_possible_commit_timestamp = isoparse(_oldest_possible_commit_timestamp)

        _additional_properties = d.pop("additionalProperties", UNSET)
        additional_properties: Union[Unset, NessieConfigurationAdditionalProperties]
        if isinstance(_additional_properties, Unset):
            additional_properties = UNSET
        else:
            additional_properties = NessieConfigurationAdditionalProperties.from_dict(_additional_properties)

        nessie_configuration = cls(
            default_branch=default_branch,
            min_supported_api_version=min_supported_api_version,
            max_supported_api_version=max_supported_api_version,
            actual_api_version=actual_api_version,
            spec_version=spec_version,
            no_ancestor_hash=no_ancestor_hash,
            repository_creation_timestamp=repository_creation_timestamp,
            oldest_possible_commit_timestamp=oldest_possible_commit_timestamp,
            additional_properties=additional_properties,
        )

        nessie_configuration.additional_properties = d
        return nessie_configuration

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
