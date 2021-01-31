import abc


class BaseStatistics(abc.ABC):
    @abc.abstractmethod
    def __init__(self):
        pass

    @abc.abstractmethod
    def get_name(self):
        pass

    @abc.abstractmethod
    def calculate_row(self, dataframe, row_index):
        pass

    @abc.abstractmethod
    def calculate_all(self, dataframe):
        pass
