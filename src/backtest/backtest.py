from src.backtest.account import Account
from src.strategies.base_strategy import BaseStrategy
from src.data.data_stream import DataStream
from src.backtest.trade_log import TradeLog
from src.strategies.test_strategy import TestStrategy
import pandas as pd
from src.data.io import Load
from src.utils.plot import Plot


class BackTest:
    def __init__(self,
                 data_set: tuple = ('BTCUSDT', '3d'),
                 commission: tuple = ('per-trade', 0),
                 starting_account: float = 10000,
                 verbose: int = 1):
        self.data_frame = Load.load_file_from_tuple(
            symbol=data_set[0], interval=data_set[1])
        self.__commision = commission
        self.__verbose = verbose
        self.__starting_account = starting_account

    def run(self, strategy: BaseStrategy = None, start_time=None, end_time=None):
        data = DataStream(
            self.data_frame, start_time=start_time, end_time=end_time)

        account = Account(starting_budget=self.__starting_account)
        trade_log = TradeLog()
        while not data.isEmpty():
            market_data = data.next()
            if strategy:
                action = strategy.execute(
                    market_data=market_data, trade_log=trade_log, account=account)
                # TODO: Add commission
                if action['type'] == 'buy':
                    account.subtract_budget(
                        market_data['Close'] * action['amount'])
                    account.add_asset(action['amount'])
                elif action['type'] == 'sell':
                    account.add_budget(
                        market_data['Close'] * action['amount'])
                    account.subtract_asset(asset=action['amount'])
                trade_log.log(market_data, action, account)
        print(trade_log.length())
        print(account.get_account_value(market_data['Close']))
        # print(trade_log.get_history_market_data().index)
        Plot.plot_trade_log(trade_log)
        # self.__log.
        # pass


if __name__ == "__main__":
    strategy = TestStrategy()
    bt = BackTest(data_set=(
        'ETHUSDT', '1w'))
    bt.run(strategy=strategy)
