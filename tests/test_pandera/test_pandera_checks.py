import pandas as pd
import pandera as pa
import pytest


@pytest.fixture(scope="class")
def sample_dataframe():
    return pd.DataFrame({
        'numerical_column': [1.1, 2.5, 3.6, 4.8, 1.1, -2.5, 3.6, 0],
        'constant_column': [0, 0, 0, 0, 0, 0, 0, 0],
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

    def test_equal_to(self, sample_dataframe):
        valid_schema = pa.DataFrameSchema({
            "constant_column": pa.Column(int, pa.Check.equal_to(value=0))
        })
        valid_schema.validate(sample_dataframe)

        invalid_schema = pa.DataFrameSchema({
            "constant_column": pa.Column(int, pa.Check.equal_to(value=5))
        })
        with pytest.raises(pa.errors.SchemaError):
            invalid_schema.validate(sample_dataframe)

    def test_isin(self, sample_dataframe):
        valid_schema = pa.DataFrameSchema({
            "constant_column": pa.Column(int, pa.Check.isin(allowed_values=[0, 1, 2]))
        })
        valid_schema.validate(sample_dataframe)

        invalid_schema = pa.DataFrameSchema({
            "numerical_column": pa.Column(int, pa.Check.isin(allowed_values=[1.1, 2.5, 3.6]))
        })
        with pytest.raises(pa.errors.SchemaError):
            invalid_schema.validate(sample_dataframe)
