import pandera as pa
import pandas as pd
import pytest


class TestPanderaColumn:

    def test_column_dtype(self):
        df = pd.DataFrame({
            "A": ["a", "b", "c"],
        })

        pa_column_valid_check = pa.Column(dtype="str")
        valid_schema = pa.DataFrameSchema({"A": pa_column_valid_check})
        _ = valid_schema.validate(df)

        pa_column_invalid_check = pa.Column(dtype="int")
        invalid_schema = pa.DataFrameSchema({"A": pa_column_invalid_check})
        with pytest.raises(pa.errors.SchemaError):
            _ = invalid_schema.validate(df)

    def test_column_checks(self):
        pass

    def test_column_parsers(self):
        pass

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
