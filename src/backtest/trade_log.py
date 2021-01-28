import pandas as pd
from src.data.io import Load


class TradeLog:

    def __init__(self):
        self.__history_market_data = pd.DataFrame(columns=['Open time', 'Open', 'High', 'Low', 'Close',
                                                           'Volume', 'Close time', 'Quote asset volume',
                                                           'Number of trades', 'Taker buy base asset volume',
                                                           'Taker buy quote asset volume'])
        self.__history_market_data.set_index('Open time', inplace=True)
        self.__accounts = []
        self.__actions = []

    def log(self, market_data, action, account):
        self.__history_market_data.loc[market_data.name] = market_data.to_dict(
        )
        self.__accounts.append(account.get_account(market_data['Close']))
        self.__actions.append(action)

    def get_log_at_index(self, index):
        return {}

    def get_accounts(self):
        return self.__accounts

    def get_account_values(self):
        return [item['value'] for item in self.__accounts]

    def get_history_market_data(self):
        return self.__history_market_data

    def get_actions(self):
        return self.__actions

    def length(self):
        return len(self.__actions)


if __name__ == '__main__':
    pass
