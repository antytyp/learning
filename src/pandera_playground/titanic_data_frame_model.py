import pandera as pa
from pandera.typing import Series

# pa.Field arguments explained:
# -> eq - whether column values are equal to given value.
# -> ne - whether column values are not equal to given value.
# -> gt - whether column values are greater than given value.
# -> ge - whether column values are greater than or equal to given value.
# -> lt - whether column values are lower than given value.
# -> le - whether column values are lower than or equal to given value.
# -> in_range - whether column values belong to given range.
# -> isin - whether column values belong to given collection.
# -> notin - whether column values do not belong to given collection.
# -> str_contains - whether column string values contain given value.
# -> str_endswith - whether column string values end with given value.
# -> str_length - whether column string values have given length.
# -> str_matches - whether column string values match given regex.
# -> str_startswith - whether column string values start with given value.
# -> nullable - whether or not the column/index can contain null values.
# -> unique - whether column values should be unique.
# -> coerce - coerces the data type if True.
# -> regex - whether or not the field name or alias is a regex pattern.
# -> ignore_na - whether or not to ignore null values in the checks.
# -> raise_warning - raise a warning instead of an Exception.
# -> n_failure_cases - report the first n unique failure cases. If None, report all failure cases.
# -> alias - the public name of the column/index.
# -> check_name - whether to check the name of the column/index during validation. None is the default behavior, which
# translates to True for columns and multi-index, and to False for a single index.
# -> dtype_kwargs - the parameters to be forwarded to the type of the field.
# -> title - a human-readable label for the field.
# -> description - an arbitrary textual description of the field.
# -> default - optional default value of the field.
# -> metadata - an optional key-value data.
# -> kwargs - specify custom checks that have been registered with the register_check_method decorator.


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
