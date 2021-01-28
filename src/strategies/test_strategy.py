from src.strategies.base_strategy import BaseStrategy


class TestStrategy(BaseStrategy):

    def __init__(self, test=True):
        self.__test = True

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
