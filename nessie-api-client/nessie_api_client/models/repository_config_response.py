from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.garbage_collector_config_object import GarbageCollectorConfigObject


T = TypeVar("T", bound="RepositoryConfigResponse")


@_attrs_define
class RepositoryConfigResponse:
    """
    Attributes:
        configs (Union[Unset, List['GarbageCollectorConfigObject']]): The existing configuration objects for the
            requested types will be returned. Non-existing config objects will not be returned.
    """

    configs: Union[Unset, List["GarbageCollectorConfigObject"]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        configs: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.configs, Unset):
            configs = []
            for configs_item_data in self.configs:
                configs_item = configs_item_data.to_dict()

                configs.append(configs_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if configs is not UNSET:
            field_dict["configs"] = configs

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.garbage_collector_config_object import GarbageCollectorConfigObject

        d = src_dict.copy()
        configs = []
        _configs = d.pop("configs", UNSET)
        for configs_item_data in _configs or []:
            configs_item = GarbageCollectorConfigObject.from_dict(configs_item_data)

            configs.append(configs_item)

        repository_config_response = cls(
            configs=configs,
        )

        repository_config_response.additional_properties = d
        return repository_config_response

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
