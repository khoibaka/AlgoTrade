from src.statistics.base_statistics import BaseStatistics
from src.data.io import Load


class MovingAverage(BaseStatistics):

    def __init__(self, window):
        self.__window = window

    def get_name(self):
        return f'{self.__window} Moving Average'

    def calculate_row(self, dataframe, row_index):
        if row_index > len(dataframe.index):
            return None
        row_index = row_index % len(dataframe.index)
        if self.__window > row_index + 1:
            ma = float('nan')
        else:
            ma = dataframe.iloc[row_index - self.__window +
                                1: row_index + 1, dataframe.columns.get_loc('Close')].mean()

        dataframe.iloc[row_index, dataframe.columns.get_loc(
            self.get_name())] = ma
        return dataframe

    def calculate_all(self, dataframe):
        dataframe[self.get_name()] = dataframe['Close'].rolling(3).mean()
        return dataframe


if __name__ == '__main__':
    df = Load.load_file(
        'F:\Projects\AlgoTradeStorage\CSV\BNBUSDT_3d.csv')
    df = df.head(10)
    ma = MovingAverage(3)
    df = ma.calculate_all(df)
    print(df)
    df['3 Moving Average'] = 1
    df = ma.calculate_row(df, -1)
    print(df)
