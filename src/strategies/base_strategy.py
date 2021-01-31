import abc


class BaseStrategy(abc.ABC):
    @abc.abstractmethod
    def __init__(self):
        pass

    @abc.abstractmethod
    def get_statistics_uses(self):
        pass

    @abc.abstractmethod
    def execute(self, market_data, trade_log, account):
        pass
