from src.strategies.base_strategy import BaseStrategy
from src.statistics.factory import Factory


class TestStrategy(BaseStrategy):

    def __init__(self, test=True):
        self.__test = True
        self.___statistics = [
            Factory.get_statistics('Moving Average', window=3)
        ]

    def get_statistics_uses(self):
        return self.___statistics

    # TODO: move action into a class itself
    def execute(self, market_data=None, trade_log=None, account=None):
        if(trade_log.length() % 2 == 0):
            return {
                'type': 'buy',
                'amount': 1
            }
        else:
            return {
                'type': 'sell',
                'amount': 1
            }
