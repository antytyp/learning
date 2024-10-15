import pandera as pa
import pandas as pd
import pytest


class TestPanderaColumn:

    def test_column_dtype(self):
        column_validator = pa.Column(dtype="str")
        schema = pa.DataFrameSchema({"A": column_validator})

        valid_df = pd.DataFrame({
            "A": ["a", "b", "c"],
        })
        _ = schema.validate(valid_df)

        invalid_df = pd.DataFrame({
            "A": [1, 2, 3],
        })
        with pytest.raises(pa.errors.SchemaError):
            _ = schema.validate(invalid_df)

    def test_column_checks(self):
        column_validator = pa.Column(
            checks=pa.Check(check_fn=lambda x: x % 5 == 0)
        )
        schema = pa.DataFrameSchema({"A": column_validator})

        valid_df = pd.DataFrame({
            "A": [5, 10, 15],
        })
        _ = schema.validate(valid_df)

        invalid_df = pd.DataFrame({
            "A": [5, 11, 15],
        })
        with pytest.raises(pa.errors.SchemaError):
            _ = schema.validate(invalid_df)

    def test_column_parsers(self):
        # Purpose: The parsers argument is a dictionary that allows you to customize the parsing of inputs before
        # they are passed to your check function. This can be useful when you need to manipulate or extract certain
        # aspects of the data before applying the check.
        column_validator = pa.Column(
            checks=pa.Check(check_fn=lambda series: series.is_unique),
            parsers=pa.Parser(lambda x: x.str.lower())
        )
        schema = pa.DataFrameSchema({"A": column_validator})

        valid_df = pd.DataFrame({
            "A": ["a", "B", "c"],
        })
        _ = schema.validate(valid_df)

        invalid_df = pd.DataFrame({
            "A": ["a", "B", "b"],
        })
        with pytest.raises(pa.errors.SchemaError):
            _ = schema.validate(invalid_df)

    def test_column_nullable(self):
        pass

    def test_column_unique(self):
        pass

    def test_column_report_nullables(self):
        pass

    def test_column_coerce(self):
        pass

    def test_column_required(self):
        pass

    def test_column_name(self):
        pass

    def test_column_regex(self):
        pass

    def test_column_title(self):
        pass

    def test_column_description(self):
        pass

    def test_column_default(self):
        pass

    def test_column_metadata(self):
        pass

    def test_column_drop_invalid_rows(self):
        pass
