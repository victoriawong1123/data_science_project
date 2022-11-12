import pandas as pd


MA_ACQUIRING_FILE = r'../data/MA_acquiring.csv'
QUARTERLY_FILE = r'../data/quarterly.csv'


def clean_df(df, drop_empty):
    if drop_empty:
        df.dropna(inpalce=True)
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
