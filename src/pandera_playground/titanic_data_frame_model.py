import pandera as pa
from pandera.typing import Series

# pa.Field arguments explained:
# eq: Optional[Any] = None, - TODO
# ne: Optional[Any] = None, - TODO
# gt: Optional[Any] = None, - TODO
# ge: Optional[Any] = None, - TODO
# lt: Optional[Any] = None, - TODO
# le: Optional[Any] = None, - TODO
# in_range: Optional[Dict[str, Any]] = None, - TODO
# isin: Optional[Iterable] = None, - TODO
# notin: Optional[Iterable] = None, - TODO
# str_contains: Optional[str] = None, - TODO
# str_endswith: Optional[str] = None, - TODO
# str_length: Optional[Dict[str, Any]] = None, - TODO
# str_matches: Optional[str] = None, - TODO
# str_startswith: Optional[str] = None, - TODO
# nullable: bool = False, - TODO
# unique: bool = False, - TODO
# coerce: bool = False, - TODO
# regex: bool = False, - TODO
# ignore_na: bool = True, - TODO
# raise_warning: bool = False, - TODO
# n_failure_cases: Optional[int] = None, - TODO
# alias: Optional[Any] = None, - TODO
# check_name: Optional[bool] = None, - TODO
# dtype_kwargs: Optional[Dict[str, Any]] = None, - TODO
# title: Optional[str] = None, - TODO
# description: Optional[str] = None, - TODO
# default: Optional[Any] = None, - TODO
# metadata: Optional[dict] = None, - TODO


class TitanicDataFrameModel(pa.DataFrameModel):
    PassengerId: Series[int] = pa.Field(ge=1)
    Survived: Series[int] = pa.Field(isin=[0, 1])
    Pclass: Series[int] = pa.Field(isin=[1, 2, 3])
    Name: Series[str] = pa.Field()
    Sex: Series[str] = pa.Field(isin=["male", "female"])
    Age: Series[float] = pa.Field(ge=0, nullable=True)
    SibSp: Series[int] = pa.Field(ge=0)
    Parch: Series[int] = pa.Field(ge=0)
    Ticket: Series[str] = pa.Field()
    Fare: Series[float] = pa.Field(ge=0)
    Cabin: Series[str] = pa.Field(nullable=True)
    Embarked: Series[str] = pa.Field(isin=["C", "Q", "S"], nullable=True)
