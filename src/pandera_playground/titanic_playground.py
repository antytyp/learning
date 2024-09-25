import pandas as pd
import pandera as pa

from titanic_data_frame_schema import titanic_schema

TITANIC_SAMPLE_DATA_PATH = '../data/titanic_sample.csv'


def get_titanic_sample_data() -> pd.DataFrame:
    return pd.read_csv(TITANIC_SAMPLE_DATA_PATH)


def main() -> None:
    titanic_df = get_titanic_sample_data()

    try:
        titanic_schema.validate(titanic_df)
    except pa.errors.SchemaError as exc:
        print(exc)


if __name__ == '__main__':
    main()
