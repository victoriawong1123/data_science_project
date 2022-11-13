from pandas import DataFrame
import numpy as np


def df_to_array(df: DataFrame, keys: list) -> np.ndarray:
    """Concert DataFrame to a matrix"""
    x = []
    for key in keys:
        if key not in df.keys():
            raise KeyError(f'{key} can not be found from DataFrame.')
        x.append(df[key].values)
    return np.asarray(x).T


def df_to_XY(df: DataFrame, xkeys: list, ykeys: list) -> tuple:
    """Concert DataFrame to a matrix X and Y"""
    return df_to_array(df, xkeys), df_to_array(df, ykeys)
