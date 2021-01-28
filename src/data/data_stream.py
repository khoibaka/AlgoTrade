from src.data.io import Load


class DataStream():
    def __init__(self, data_frame, start_time=None, end_time=None):

        self.__start_time = start_time
        self.__end_time = end_time
        mask = True
        if start_time:
            mask = mask & (data_frame['Open time'] > start_time)
        if end_time:
            mask = mask & (data_frame['End time'] < end_time)
        if end_time or start_time:
            self.__data = data_frame.loc[mask]
        else:
            self.__data = data_frame
        self.__index = 0
        self.__length = len(self.__data.index)

    def next(self):
        if(self.isEmpty()):
            raise IndexError("No more data")
        value = self.__data.iloc[self.__index, :]
        self.__index += 1
        return value

    def getItem(self, index):
        return self.__data.iloc[index, :]

    def isEmpty(self):
        return self.__index == self.__length

    def get_data(self):
        return self.__data

    def reset(self):
        self.__index = 0

    def get_index(self):
        return self.__index


if __name__ == "__main__":
    data_frame = Load.load_file(
        'F:\Projects\AlgoTradeStorage\CSV\BNBUSDT_11-06-17_08-17-20_1d.csv')
    data_stream = DataStream(data_frame)
