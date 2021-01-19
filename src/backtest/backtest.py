from .account import Account
from src.strategies.base_strategy import BaseStrategy


class BackTest:
    def __init__(self,
                 data_set: tuple = ('BTCUSDT', '1h', '08-17-2017', '08-17-2020'),
                 strategy: BaseStrategy = None,
                 commission: tuple = ('per-trade', 0),
                 starting_account: float = 10000,
                 verbose: int = 1):
        self.__account = Account(starting_budget=starting_account)
