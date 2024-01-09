from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="UDFV1")


@_attrs_define
class UDFV1:
    """
    Attributes:
        sql_text (str):
        id (Union[Unset, str]):
        dialect (Union[Unset, str]):
    """

    sql_text: str
    id: Union[Unset, str] = UNSET
    dialect: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        sql_text = self.sql_text
        id = self.id
        dialect = self.dialect

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "sqlText": sql_text,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if dialect is not UNSET:
            field_dict["dialect"] = dialect

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        sql_text = d.pop("sqlText")

        id = d.pop("id", UNSET)

        dialect = d.pop("dialect", UNSET)

        udfv1 = cls(
            sql_text=sql_text,
            id=id,
            dialect=dialect,
        )

        udfv1.additional_properties = d
        return udfv1

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
