import pandera as pa

# pa.DataFrameSchema arguments explained:
# columns: Optional[Dict[Any, Any]] = None, - defines the schema for individual columns using pa.Column
# checks: Optional[CheckList] = None, - allows validation rules for the entire DataFrame
# parsers: Optional[ParserList] = None, - TODO
# index = None, - defines validation rules for the DataFrame’s index
# dtype: Optional[Any] = None, - TODO
# coerce: bool = False, - automatically converts columns to the specified data types
# strict: StrictType = False, - disallows columns not defined in the schema
# name: Optional[str] = None, - gives the schema a custom name for easier logging and debugging
# ordered: bool = False, - ensures that the DataFrame columns match the schema’s column order
# unique: Optional[Union[str, List[str]]] = None, - TODO
# report_duplicates: UniqueSettings = "all", - TODO
# unique_column_names: bool = False, - TODO
# add_missing_columns: bool = False, - TODO
# title: Optional[str] = None, - TODO
# description: Optional[str] = None, - TODO
# metadata: Optional[dict] = None, - TODO
# drop_invalid_rows: bool = False, - TODO

# pa.Column arguments explained:
# dtype: PandasDtypeInputTypes = None, - specifies the data type
# checks: Optional[CheckList] = None, - defines validation rules
# parsers: Optional[ParserList] = None, - TODO
# nullable: bool = False, - allows or disallows NaN values
# unique: bool = False, - ensures uniqueness of values
# report_duplicates: UniqueSettings = "all", - TODO
# coerce: bool = False, - automatically converts values to the specified type
# required: bool = True, - makes the column mandatory or optional
# name: Union[str, Tuple[str, ...], None] = None, - TODO
# regex: bool = False, - matches column names with regex
# title: Optional[str] = None, - TODO
# description: Optional[str] = None, - TODO
# default: Optional[Any] = None, - TODO
# metadata: Optional[dict] = None, - TODO
# drop_invalid_rows: bool = False, - TODO

# pa.Check arguments explained:
# check_fn: Callable, - TODO
# groups: Optional[Union[str, List[str]]] = None, - TODO
# groupby: Optional[Union[str, List[str], Callable]] = None, - TODO
# ignore_na: bool = True, - TODO
# element_wise: bool = False, - TODO
# name: Optional[str] = None, - TODO
# error: Optional[str] = None, - TODO
# raise_warning: bool = False, - TODO
# n_failure_cases: Optional[int] = None, - TODO
# title: Optional[str] = None, - TODO
# description: Optional[str] = None, - TODO
# statistics: Optional[Dict[str, Any]] = None, - TODO
# strategy: Optional[Any] = None, - TODO
# ** check_kwargs, - TODO


titanic_schema = pa.DataFrameSchema(
    columns={
        "PassengerId": pa.Column(int, checks=pa.Check.greater_than_or_equal_to(1), nullable=False),
        "Survived": pa.Column(int, checks=pa.Check.isin([0, 1]), nullable=False),
        "Pclass": pa.Column(int, checks=pa.Check.isin([1, 2, 3]), nullable=False),
        "Name": pa.Column(str, nullable=False),
        "Sex": pa.Column(str, checks=pa.Check.isin(['male', 'female']), nullable=False),
        "Age": pa.Column(float, checks=pa.Check.greater_than_or_equal_to(0), nullable=True),
        "SibSp": pa.Column(int, checks=pa.Check.greater_than_or_equal_to(0), nullable=False),
        "Parch": pa.Column(int, checks=pa.Check.greater_than_or_equal_to(0), nullable=False),
        "Ticket": pa.Column(str, nullable=False),
        "Fare": pa.Column(float, checks=pa.Check.greater_than_or_equal_to(0), nullable=False),
        "Cabin": pa.Column(str, nullable=True),
        "Embarked": pa.Column(str, checks=pa.Check.isin(["C", "Q", "S"]), nullable=True),
    }
)
