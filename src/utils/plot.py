import mplfinance as mpf
from src.data.io import Load
import matplotlib.pyplot as plt


class Plot:
    @staticmethod
    def plot_market(market_data, actions, axis=None):
        vlines = []
        colors = []
        for index, action in enumerate(actions):
            if action['type'] == 'buy':
                vlines.append(market_data.index[index])
                colors.append('b')
            elif action['type'] == 'sell':
                vlines.append(market_data.index[index])
                colors.append('r')

        print(actions[:10])
        mpf.plot(market_data, type='candle', vlines=dict(
            vlines=vlines, colors=colors, alpha=1, linewidths=1), ax=axis)

    @staticmethod
    def plot_account(open_time, accounts, axis=None):
        axis.plot(open_time, accounts)

    @staticmethod
    def plot_trade_log(trade_log):
        fig, (ax1, ax2) = plt.subplots(2)
        Plot.plot_market(trade_log.get_history_market_data(),
                         trade_log.get_actions(), axis=ax1)
        Plot.plot_account(trade_log.get_history_market_data(
        ).index.to_list(), trade_log.get_account_values(), axis=ax2)
        plt.show()


if __name__ == "__main__":
    df = Load.load_file(
        'F:\Projects\AlgoTradeStorage\CSV\BNBUSDT_3d.csv')
    Plot.plot_market(df)
