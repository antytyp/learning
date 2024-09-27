import pandas as pd
import pandera as pa
import pytest


@pytest.fixture(scope="class")
def sample_dataframe():
    return pd.DataFrame({
        'numerical_column': [1.1, 2.5, 3.6, 4.8, 1.1, -2.5, 3.6, 0],
    })


class TestPanderaChecks:

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

    def test_check_in_range(self):
        schema = pa.DataFrameSchema({
            "range_column": pa.Column(int, pa.Check.in_range(1, 10))
        })

        valid_df = pd.DataFrame({
            "range_column": [1, 5, 8, 10]
        })

        invalid_df = pd.DataFrame({
            "range_column": [0, 11, 5]
        })

        schema.validate(valid_df)

        with pytest.raises(pa.errors.SchemaError):
            schema.validate(invalid_df)
