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
        column_validator = pa.Column(
            nullable=False,
        )
        schema = pa.DataFrameSchema({"A": column_validator})

        valid_df = pd.DataFrame({
            "A": [1, 2, 3],
        })
        _ = schema.validate(valid_df)

        invalid_df = pd.DataFrame({
            "A": [1, None, 3],
        })
        with pytest.raises(pa.errors.SchemaError):
            _ = schema.validate(invalid_df)

    def test_column_unique(self):
        column_validator = pa.Column(
            unique=True,
        )
        schema = pa.DataFrameSchema({"A": column_validator})

        valid_df = pd.DataFrame({
            "A": [1, 2, 3],
        })
        _ = schema.validate(valid_df)

        invalid_df = pd.DataFrame({
            "A": [1, 2, 2],
        })
        with pytest.raises(pa.errors.SchemaError):
            _ = schema.validate(invalid_df)

    def test_column_report_duplicates(self):
        # (Union[Literal[‘exclude_first’], Literal[‘exclude_last’], Literal[‘all’]]) – how to report unique errors -
        # exclude_first: report all duplicates except first occurence - exclude_last: report all duplicates except
        # last occurence - all: (default) report all duplicates
        pass

    def test_column_coerce(self):
        column_validator = pa.Column(
            dtype=int,
            coerce=True,
        )
        schema = pa.DataFrameSchema({"A": column_validator})

        df = pd.DataFrame({
            "A": ["1", "2", "3"],
        })
        assert df["A"].dtype != 'int64'
        validated_df = schema.validate(df)
        assert validated_df["A"].dtype == 'int64'

    def test_column_required(self):
        column_validator = pa.Column(
            required=True,
        )
        schema = pa.DataFrameSchema({"A": column_validator})

        valid_df = pd.DataFrame({
            "A": [1, 2, 3],
            "B": [4, 5, 6],
        })
        _ = schema.validate(valid_df)

        invalid_df = pd.DataFrame({
            "B": [4, 5, 6],
            "C": [1, 2, 3],
        })
        with pytest.raises(pa.errors.SchemaError):
            _ = schema.validate(invalid_df)

    def test_column_name(self):
        column_validator = pa.Column(
            unique=True,
            name="A",
        )

        valid_df = pd.DataFrame({
            "A": [1, 2, 3],
            "B": [1, 3, 3]
        })
        _ = column_validator.validate(valid_df)

        invalid_df = pd.DataFrame({
            "A": [1, 2, 2],
            "B": [1, 3, 3]
        })
        with pytest.raises(pa.errors.SchemaError):
            _ = column_validator.validate(invalid_df)

    def test_column_regex(self):
        column_validator = pa.Column(
            unique=True,
            name="A.+",
            regex=True,
        )
        valid_df = pd.DataFrame({
            "A1": [1, 2, 3],
            "A2": [1, 2, 3],
            "B": [1, 3, 3]
        })
        _ = column_validator.validate(valid_df)

        invalid_df1 = pd.DataFrame({
            "A1": [1, 2, 2],
            "B": [1, 3, 3]
        })
        invalid_df2 = pd.DataFrame({
            "A2": [1, 1, 2],
            "B": [1, 3, 3]
        })
        with pytest.raises(pa.errors.SchemaError):
            _ = column_validator.validate(invalid_df1)
            _ = column_validator.validate(invalid_df2)

    def test_column_title(self):
        schema = pa.DataFrameSchema({
            "salary": pa.Column(title="Annual Salary"),
        })

    def test_column_description(self):
        schema = pa.DataFrameSchema({
            "age": pa.Column(description="The age of the individual in full years."),
        })

    def test_column_default(self):
        column_validator = pa.Column(
            default=0.0,
        )
        schema = pa.DataFrameSchema({"A": column_validator})

        df = pd.DataFrame({
            "A": [1.0, None, 3.0],
        })
        validated_df = schema.validate(df)
        expected_validated_df = pd.DataFrame({
            "A": [1.0, 0.0, 3.0],
        })
        pd.testing.assert_frame_equal(
            validated_df,
            expected_validated_df,
        )

    def test_column_metadata(self):
        metadata = {
            "source": "user-input",
            "privacy_level": "non-sensitive",
            "to_be_normalized": False
        }
        column_validator = pa.Column(
            metadata=metadata
        )
        schema = pa.DataFrameSchema({"age": column_validator})
        assert schema.columns["age"].metadata == metadata

    def test_column_drop_invalid_rows(self):
        column_validator = pa.Column(
            name="A",
            drop_invalid_rows=True,
            checks=pa.Check(check_fn=lambda x: x % 5 == 0),
        )
        df = pd.DataFrame({
            "A": [5, 10, 12, 15]
        })
        validated_df = column_validator.validate(df, lazy=True)
        expected_validated_df = pd.DataFrame({
            "A": [5, 10, 15]
        })
        pd.testing.assert_frame_equal(
            validated_df.reset_index(drop=True),
            expected_validated_df.reset_index(drop=True)
        )
