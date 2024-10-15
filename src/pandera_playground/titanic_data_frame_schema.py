import pandera as pa

# pa.DataFrameSchema arguments explained:
# -> columns – a dict where keys are column names and values are Column objects, specifying the datatypes and properties
# of a particular column.
# -> checks - dataframe-wide checks.
# -> parsers - dataframe-wide parsers.
# -> index - specify the datatypes and properties of the index.
# -> dtype -  datatype of the dataframe. This overrides the data types specified in any of the columns. If a string is
# specified, then assumes one of the valid pandas string values:
# http://pandas.pydata.org/pandas-docs/stable/basics.html#dtypes.
# -> coerce - whether or not to coerce all of the columns on validation. This overrides any coerce setting at the
# column or index level. This has no effect on columns where dtype=None.
# -> strict - ensure that all and only the columns defined in the schema are present in the dataframe. If set to
# ‘filter’, only the columns in the schema will be passed to the validated dataframe. If set to filter and columns
# defined in the schema are not present in the dataframe, will throw an error.
# -> name - name of the schema.
# -> ordered - whether or not to validate the columns order.
# -> unique - a list of columns that should be jointly unique.
# -> report_duplicates -  how to report unique errors - exclude_first: report all duplicates except first occurence
# - exclude_last: report all duplicates except last occurence - all: (default) report all duplicates
# -> unique_column_names - whether or not column names must be unique.
# -> add_missing_columns - add missing column names with either default value, if specified in column schema, or NaN if
# column is nullable.
# -> title - a human-readable label for the schema.
# -> description - an arbitrary textual description of the schema.
# -> metadata - an optional key-value data.
# -> drop_invalid_rows - if True, drop invalid rows on validation.

# pa.Check arguments explained:
# -> check_fn - a function to check data object. For Column or SeriesSchema checks, if element_wise is True, this
# function should have the signature: Callable[[pd.Series], Union[pd.Series, bool]], where the output series is a
# boolean vector.
# -> groups - the dict input to the fn callable will be constrained to the groups specified by groups.
# -> groupby - if a string or list of strings is provided, these columns are used to group the Column series. If a
# callable is passed, the expected signature is: Callable[ [pd.DataFrame], pd.core.groupby.DataFrameGroupBy].
# -> ignore_na - if True, null values will be ignored when determining if a check passed or failed. For dataframes,
# ignores rows with any null value.
# -> element_wise - whether or not to apply validator in an element-wise fashion. If bool, assumes that all checks
# should be applied to the column element-wise. If list, should be the same number of elements as checks.
# -> name - optional name for the check.
# -> error - custom error message if series fails validation check.
# -> raise_warning - if True, raise a SchemaWarning and do not throw exception instead of raising a SchemaError for a
# specific check. This option should be used carefully in cases where a failing check is informational and shouldn’t
# stop execution of the program.
# -> n_failure_cases - report the first n unique failure cases. If None, report all failure cases.
# -> title - a human-readable label for the check.
# -> description - an arbitrary textual description of the check.
# -> statistics - kwargs to pass into the check function. These values are serialized and represent the constraints
# of the checks.
# -> strategy - a hypothesis strategy, used for implementing data synthesis strategies for this check.
# -> ** check_kwargs - key-word arguments to pass into check_fn.


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
