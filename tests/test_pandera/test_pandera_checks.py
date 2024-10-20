import pandas as pd
import pandera as pa
import pytest


class TestPanderaCheck:

    def test_check_between(self):
        check = pa.Check.between(min_value=10, max_value=15)
        schema = pa.DataFrameSchema(columns={"A": pa.Column(int, checks=check)})

        valid_df = pd.DataFrame({
            "A": [10, 11, 12, 13, 14, 15],
        })
        _ = schema.validate(valid_df)

        invalid_df = pd.DataFrame({
            "A": [8, 10, 12, 15, 16],
        })
        with pytest.raises(pa.errors.SchemaError):
            _ = schema.validate(invalid_df)

    def test_check_eq(self):
        check = pa.Check.eq(value='const')
        schema = pa.DataFrameSchema(columns={"A": pa.Column(str, checks=check)})

        valid_df = pd.DataFrame({
            "A": ['const', 'const', 'const']
        })
        _ = schema.validate(valid_df)

        invalid_df = pd.DataFrame({
            "A": ['a', 'const', 'c'],
        })
        with pytest.raises(pa.errors.SchemaError):
            _ = schema.validate(invalid_df)

    def test_check_equal_to(self):
        check = pa.Check.equal_to(value='const')
        schema = pa.DataFrameSchema(columns={"A": pa.Column(str, checks=check)})

        valid_df = pd.DataFrame({
            "A": ['const', 'const', 'const']
        })
        _ = schema.validate(valid_df)

        invalid_df = pd.DataFrame({
            "A": ['a', 'const', 'c'],
        })
        with pytest.raises(pa.errors.SchemaError):
            _ = schema.validate(invalid_df)

    def test_check_ge(self):
        check = pa.Check.ge(min_value=5.0)
        schema = pa.DataFrameSchema(columns={"A": pa.Column(float, checks=check)})

        valid_df = pd.DataFrame({
            "A": [5.0, 10.0, 15.0],
        })
        _ = schema.validate(valid_df)

        invalid_df = pd.DataFrame({
            "A": [3.0, 5.0, 9.0]
        })
        with pytest.raises(pa.errors.SchemaError):
            _ = schema.validate(invalid_df)

    def test_check_greater_than(self):
        check = pa.Check.greater_than(5.0)
        schema = pa.DataFrameSchema(columns={"A": pa.Column(float, checks=check)})

        valid_df = pd.DataFrame({
            "A": [6.0, 10.0, 15.0],
        })
        _ = schema.validate(valid_df)

        invalid_df = pd.DataFrame({
            "A": [5.0, 6.0, 9.0]
        })
        with pytest.raises(pa.errors.SchemaError):
            _ = schema.validate(invalid_df)

    def test_check_greater_than_or_eqal_to(self):
        check = pa.Check.greater_than_or_equal_to(5.0)
        schema = pa.DataFrameSchema(columns={"A": pa.Column(float, checks=check)})

        valid_df = pd.DataFrame({
            "A": [5.0, 10.0, 15.0],
        })
        _ = schema.validate(valid_df)

        invalid_df = pd.DataFrame({
            "A": [3.0, 5.0, 9.0]
        })
        with pytest.raises(pa.errors.SchemaError):
            _ = schema.validate(invalid_df)

    def test_check_gt(self):
        check = pa.Check.gt(5.0)
        schema = pa.DataFrameSchema(columns={"A": pa.Column(float, checks=check)})

        valid_df = pd.DataFrame({
            "A": [6.0, 10.0, 15.0],
        })
        _ = schema.validate(valid_df)

        invalid_df = pd.DataFrame({
            "A": [5.0, 6.0, 9.0]
        })
        with pytest.raises(pa.errors.SchemaError):
            _ = schema.validate(invalid_df)

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
