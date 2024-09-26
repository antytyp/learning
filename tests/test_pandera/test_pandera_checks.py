import pandas as pd
import pandera as pa
from pandera import Check, Column, DataFrameSchema
import pytest


class TestPanderaChecks:

    def test_check_greater_than(self):
        schema = DataFrameSchema({
            "positive_column": Column(float, Check.greater_than(0))
        })

        valid_df = pd.DataFrame({
            "positive_column": [1.1, 2.5, 3.6, 4.8]
        })

        invalid_df = pd.DataFrame({
            "positive_column": [1.1, -2.5, 3.6, 0]
        })

        schema.validate(valid_df)

        with pytest.raises(pa.errors.SchemaError):
            schema.validate(invalid_df)

    def test_check_in_range(self):
        schema = DataFrameSchema({
            "range_column": Column(int, Check.in_range(1, 10))
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
