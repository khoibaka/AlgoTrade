import numpy as np
import pandas as pd
from src.utils.time_converter import TimeConverter
COLUMN_NAMES = ['Open time', 'Open', 'High', 'Low', 'Close',
                'Volume', 'Close time', 'Quote asset volume',
                'Number of trades', 'Taker buy base asset volume',
                'Taker buy quote asset volume']

def list_to_array(kline_list):
    return np.array(kline_list, dtype=np.float32)

def list_to_dataframe(kline_list):
    array = list_to_array(kline_list)
    df = pd.DataFrame(array, columns=COLUMN_NAMES)
    # df[['Open time', 'Close time']].apply(lambda time: TimeConverter.ms_to_datetime(time))
    df['Open time'] = df['Open time'].apply(TimeConverter.ms_to_datetime)
    df['Close time'] = df['Close time'].apply(TimeConverter.ms_to_datetime)
    return df

def dataframe_to_list(df):
    return df.values.tolist()

def string_list_to_number_list(string_lists):
    for index in range(len(string_lists)):
        string_list = string_lists[index]
        string_lists[index] = [int(string_list[0])] \
                              + [float(x) for x in string_list[1:6]] \
                              + [int(string_list[6])] \
                              + [float(x) for x in string_list[7:-1]]
    return string_lists
