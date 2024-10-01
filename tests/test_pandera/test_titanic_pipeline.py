import pandas as pd
import pandera as pa
import pytest

TITANIC_SAMPLE_DATA_PATH = 'data/titanic_sample.csv'


@pytest.fixture(scope="class")
def sample_titanic_dataset() -> pd.DataFrame:
    return pd.read_csv(TITANIC_SAMPLE_DATA_PATH)

@pytest.fixture(scope="class")
def initial_schema() -> pa.DataFrameSchema:
    return pa.DataFrameSchema({
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
    })

@pytest.fixture(scope="class")
def schema_without_missing_values() -> pa.DataFrameSchema:
    return pa.DataFrameSchema({
        "PassengerId": pa.Column(int, checks=pa.Check.greater_than_or_equal_to(1), nullable=False),
        "Survived": pa.Column(int, checks=pa.Check.isin([0, 1]), nullable=False),
        "Pclass": pa.Column(int, checks=pa.Check.isin([1, 2, 3]), nullable=False),
        "Name": pa.Column(str, nullable=False),
        "Sex": pa.Column(str, checks=pa.Check.isin(['male', 'female']), nullable=False),
        "Age": pa.Column(float, checks=pa.Check.greater_than_or_equal_to(0), nullable=False),
        "SibSp": pa.Column(int, checks=pa.Check.greater_than_or_equal_to(0), nullable=False),
        "Parch": pa.Column(int, checks=pa.Check.greater_than_or_equal_to(0), nullable=False),
        "Ticket": pa.Column(str, nullable=False),
        "Fare": pa.Column(float, checks=pa.Check.greater_than_or_equal_to(0), nullable=False),
        "Cabin": pa.Column(str, nullable=False),
        "Embarked": pa.Column(str, checks=pa.Check.isin(["C", "Q", "S"]), nullable=False),
    })


@pytest.fixture(scope="class")
def schema_after_encoding() -> pa.DataFrameSchema:
    return pa.DataFrameSchema({
        "PassengerId": pa.Column(int, checks=pa.Check.greater_than_or_equal_to(1), nullable=False),
        "Survived": pa.Column(int, checks=pa.Check.isin([0, 1]), nullable=False),
        "Pclass": pa.Column(int, checks=pa.Check.isin([1, 2, 3]), nullable=False),
        "Name": pa.Column(str, nullable=False),
        "Sex": pa.Column(int, checks=pa.Check.isin([0, 1]), nullable=False),
        "Age": pa.Column(float, checks=pa.Check.greater_than_or_equal_to(0), nullable=True),
        "SibSp": pa.Column(int, checks=pa.Check.greater_than_or_equal_to(0), nullable=False),
        "Parch": pa.Column(int, checks=pa.Check.greater_than_or_equal_to(0), nullable=False),
        "Ticket": pa.Column(str, nullable=False),
        "Fare": pa.Column(float, checks=pa.Check.greater_than_or_equal_to(0), nullable=False),
        "Cabin": pa.Column(str, nullable=True),
        "Embarked_Q": pa.Column(bool, checks=pa.Check.isin([True, False])),
        "Embarked_S": pa.Column(bool, checks=pa.Check.isin([True, False])),
})


class TestTitanicPipelinePanderaValidation:

    def test_handle_missing_values(self, sample_titanic_dataset, initial_schema, schema_without_missing_values):

        @pa.check_input(initial_schema)
        @pa.check_output(schema_without_missing_values)
        def _handle_missing_values(df: pd.DataFrame) -> pd.DataFrame:
            age_median = df['Age'].median()
            df['Age'].fillna(value=age_median, inplace=True)

            cabin_median = df['Cabin'].mode()[0]
            df['Cabin'].fillna(value=cabin_median, inplace=True)

            embarked_mode = df['Embarked'].mode()[0]
            df['Embarked'].fillna(value=embarked_mode, inplace=True)

            return df

        _handle_missing_values(sample_titanic_dataset)

    def test_encode_categorical_columns(self, sample_titanic_dataset, initial_schema, schema_after_encoding):

        @pa.check_input(initial_schema)
        @pa.check_output(schema_after_encoding)
        def _encode_categorical_columns(df: pd.DataFrame) -> pd.DataFrame:
            df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})

            embarked_dummies = pd.get_dummies(df['Embarked'], prefix='Embarked', drop_first=True)
            df = pd.concat([df, embarked_dummies], axis=1)
            df.drop(columns=['Embarked'], inplace=True)

            return df

        _encode_categorical_columns(sample_titanic_dataset)
