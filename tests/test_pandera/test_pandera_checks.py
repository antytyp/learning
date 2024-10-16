import pandas as pd
import pandera as pa
import pytest


@pytest.fixture(scope="class")
def sample_dataframe():
    return pd.DataFrame({
        'numerical_column': [1.1, 2.5, 3.6, 4.8, 1.1, -2.5, 3.6, 0],
        'constant_column': [0, 0, 0, 0, 0, 0, 0, 0],
        'string_column': ['aa', 'abbb', 'acc', 'a', 'bc', 'abcd', 'c', 'ab'],
    })


class TestPanderaCheck:

    def test_check_greater_than(self, sample_dataframe):
        valid_schema = pa.DataFrameSchema({
            "numerical_column": pa.Column(float, pa.Check.greater_than(-3.0))
        })
        valid_schema.validate(sample_dataframe)

        invalid_schema = pa.DataFrameSchema({
            "numerical_column": pa.Column(float, pa.Check.greater_than(0.0))
        })
        with pytest.raises(pa.errors.SchemaError):
            invalid_schema.validate(sample_dataframe)

    def test_check_in_range(self, sample_dataframe):
        valid_schema = pa.DataFrameSchema({
            "numerical_column": pa.Column(float, pa.Check.in_range(-5.0, 5.0))
        })
        valid_schema.validate(sample_dataframe)

        invalid_schema = pa.DataFrameSchema({
            "numerical_column": pa.Column(float, pa.Check.in_range(-2.0, 2.0))
        })
        with pytest.raises(pa.errors.SchemaError):
            invalid_schema.validate(sample_dataframe)

    def test_check_equal_to(self, sample_dataframe):
        valid_schema = pa.DataFrameSchema({
            "constant_column": pa.Column(int, pa.Check.equal_to(value=0))
        })
        valid_schema.validate(sample_dataframe)

        invalid_schema = pa.DataFrameSchema({
            "constant_column": pa.Column(int, pa.Check.equal_to(value=5))
        })
        with pytest.raises(pa.errors.SchemaError):
            invalid_schema.validate(sample_dataframe)

    def test_check_isin(self, sample_dataframe):
        valid_schema = pa.DataFrameSchema({
            "constant_column": pa.Column(int, pa.Check.isin(allowed_values=[0, 1, 2]))
        })
        valid_schema.validate(sample_dataframe)

        invalid_schema = pa.DataFrameSchema({
            "numerical_column": pa.Column(int, pa.Check.isin(allowed_values=[1.1, 2.5, 3.6]))
        })
        with pytest.raises(pa.errors.SchemaError):
            invalid_schema.validate(sample_dataframe)

    def test_str_length(self, sample_dataframe):
        valid_schema = pa.DataFrameSchema({
            "string_column": pa.Column(str, pa.Check.str_length(min_value=1, max_value=5))
        })
        valid_schema.validate(sample_dataframe)

        invalid_schema = pa.DataFrameSchema({
            "string_column": pa.Column(str, pa.Check.str_length(min_value=4, max_value=5))
        })
        with pytest.raises(pa.errors.SchemaError):
            invalid_schema.validate(sample_dataframe)

    def test_check_str_matches(self, sample_dataframe):
        valid_schema = pa.DataFrameSchema({
            "string_column": pa.Column(str, pa.Check.str_matches(pattern='^[abcd]+$'))
        })
        valid_schema.validate(sample_dataframe)

        invalid_schema = pa.DataFrameSchema({
            "string_column": pa.Column(str, pa.Check.str_matches(pattern='^[ad]+$'))
        })
        with pytest.raises(pa.errors.SchemaError):
            invalid_schema.validate(sample_dataframe)

    def test_check_check_fn(self):
        # check_fn - a function to check data object. For Column or SeriesSchema checks, if element_wise is True, this
        # function should have the signature: Callable[[pd.Series], Union[pd.Series, bool]], where the output series is a
        # boolean vector.
        raise NotImplementedError("Test not implemented yet")

    def test_check_groups(self):
        # groups - the dict input to the fn callable will be constrained to the groups specified by groups.
        raise NotImplementedError("Test not implemented yet")

    def test_check_groupby(self):
        # groupby - if a string or list of strings is provided, these columns are used to group the Column series. If a
        # callable is passed, the expected signature is: Callable[ [pd.DataFrame], pd.core.groupby.DataFrameGroupBy].
        raise NotImplementedError("Test not implemented yet")

    def test_check_ignore_na(self):
        # ignore_na - if True, null values will be ignored when determining if a check passed or failed. For dataframes,
        # ignores rows with any null value.
        raise NotImplementedError("Test not implemented yet")

    def test_check_element_wise(self):
        # element_wise - whether or not to apply validator in an element-wise fashion. If bool, assumes that all checks
        # should be applied to the column element-wise. If list, should be the same number of elements as checks.
        raise NotImplementedError("Test not implemented yet")

    def test_check_name(self):
        # name - optional name for the check.
        raise NotImplementedError("Test not implemented yet")

    def test_check_error(self):
        # error - custom error message if series fails validation check.
        raise NotImplementedError("Test not implemented yet")

    def test_check_raise_warning(self):
        # raise_warning - if True, raise a SchemaWarning and do not throw exception instead of raising a SchemaError for a
        # specific check. This option should be used carefully in cases where a failing check is informational and shouldn’t
        # stop execution of the program.
        raise NotImplementedError("Test not implemented yet")

    def test_check_n_failure_cases(self):
        # n_failure_cases - report the first n unique failure cases. If None, report all failure cases.
        raise NotImplementedError("Test not implemented yet")

    def test_check_title(self):
        # title - a human-readable label for the check.
        raise NotImplementedError("Test not implemented yet")

    def test_check_description(self):
        # description - an arbitrary textual description of the check.
        raise NotImplementedError("Test not implemented yet")

    def test_check_statistics(self):
        # statistics - kwargs to pass into the check function. These values are serialized and represent the constraints
        # of the checks.
        raise NotImplementedError("Test not implemented yet")

    def test_check_strategy(self):
        # strategy - a hypothesis strategy, used for implementing data synthesis strategies for this check.
        raise NotImplementedError("Test not implemented yet")

    def test_check_kwargs(self):
        # ** check_kwargs - key-word arguments to pass into check_fn.
        raise NotImplementedError("Test not implemented yet")
