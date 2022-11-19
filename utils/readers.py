import pandas as pd


MA_ACQUIRING_FILE = r'../data/MA_acquiring.csv'
QUARTERLY_FILE = r'../data/quarterly.csv'
ACQURIOR_FILE = r'../data/acquiror_uk.csv'


def clean_df(df, drop_empty):
    if drop_empty:
        df.dropna(inplace=True)
        return df.reset_index(drop=True)
    else:
        return df


def read_ma_acquiring(drop_empty=True):
    """Read M&A acquiring data."""
    df = pd.read_csv(MA_ACQUIRING_FILE)
    return clean_df(df, drop_empty)


def read_quarterly(drop_empty=True):
    """Read quarterly data"""
    df = pd.read_csv(QUARTERLY_FILE)
    return clean_df(df, drop_empty)


def read_acquiror_uk():
    """Read acquiror"""
    df = pd.read_csv(ACQURIOR_FILE)
    df['Date'] = pd.to_datetime(df['Date'], format='%d.%m.%y')
    return df

