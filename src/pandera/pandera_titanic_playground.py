import pandas as pd

TITANIC_SAMPLE_DATA_PATH = '../data/titanic_sample.csv'


def get_titanic_sample_data() -> pd.DataFrame:
    return pd.read_csv(TITANIC_SAMPLE_DATA_PATH)

def main() -> None:
    titanic_df = get_titanic_sample_data()
    print(titanic_df.shape)


if __name__ == '__main__':
    main()
