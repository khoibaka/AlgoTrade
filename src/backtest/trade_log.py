import pandas as pd
from src.data.io import Load

class TradeLog:

    def __init__(self, starting_budget):
        self.__history_market_data = pd.DataFrame(columns=['Open time', 'Open', 'High', 'Low', 'Close',
                                                           'Volume', 'Close time', 'Quote asset volume',
                                                           'Number of trades', 'Taker buy base asset volume',
                                                           'Taker buy quote asset volume'])
        self.__trade_log = []
        self.__starting_budget = starting_budget
        self.__current_budget = starting_budget
        self.__current_crypto = 0

    def log(self, market_data, action):
        self.__history_market_data = self.__history_market_data.append(market_data, ignore_index=True)
        if action['type'] == "buy":
            self.__current_budget -= market_data['Close'] * action['amount']
            self.__current_crypto += action['amount']
            self.__trade_log.append({
                'action': action,
                'budget': self.__current_budget,
                'crypto': self.__current_crypto,
                'value': self.get_current_value(),
            })
        elif action['type'] == "sell":
            self.__current_budget += market_data['Close'] * action['amount']
            self.__current_crypto -= action['amount']
            self.__trade_log.append({
                'action': action,
                'budget': self.__current_budget,
                'crypto': self.__current_crypto,
                'value': self.get_current_value(),
            })
    def get_current_budget(self):
        return self.__current_budget

    def get_current_crypto(self):
        return self.__current_crypto

    def get_current_value(self):
        print(self.__history_market_data)
        total_money = self.__current_budget + self.__current_crypto * self.__history_market_data.iloc[-1, 4]
        total_crypto = self.__current_budget / self.__history_market_data.iloc[-1, 4] + self.__current_crypto
        return {
            'budget': total_money,
            'crypto': total_crypto,
            'percent_change': (total_money - self.__starting_budget) * 100 / self.__starting_budget
        }

    def get_trade_log(self):
        return self.__trade_log

if __name__ == '__main__':
    log = TradeLog(10000)
    action = {
        'type': 'buy',
        'amount': 100
    }
    data = Load.load_file('F:\Projects\AlgoTradeStorage\CSV\BNBUSDT_11-06-17_08-17-20_1d.csv')
    for i in range(10):
        if i % 2 == 0:
            log.log(data.iloc[i, :],{
                'type': 'buy',
                'amount': 1000
            })
        else:
            log.log(data.iloc[i, :], {
                'type': 'sell',
                'amount': 1000
            })

    print(log.get_current_crypto())
    print(log.get_current_budget())
    for data_log in log.get_trade_log():
        print(data_log)
