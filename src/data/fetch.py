from binance.client import Client
from src.const.API_KEY import BINANCE


class BinanceDataFetch:

    def __init__(self):
        self.client = Client(BINANCE['API_KEY'], BINANCE['SECRET_KEY'])
        self.max_entries = 10000

    def fetch_kline_csv(self, symbol, interval, start_time, end_time=None):
        """Get kline data from Binance
            symbol: 'BTCUSDT', 'ETHUSDT', 'BNBUSDT','BNBBTC', 'ETHBTC', 'LTCBTC'
            interval: 1m, 3m, 5m, 15m, 30m, 1h, 2h, 4h, 6h, 8h, 12h, 1d, 3d, 1w
            start_time: date string
        """
        if not symbol:
            return None

        

        output_data = self.client.get_klines(
            symbol=symbol,
            interval=interval,
            startTime=start_time,
            endTime=end_time
        )
        return output_data


if __name__ == '__main__':
    print(BINANCE['API_KEY'])
    bnf = BinanceDataFetch()
    print(bnf.fetch_kline_csv('ETHUSDT', '1m', 1592390280000, 1598361300000)[0])
    print(bnf.fetch_kline_csv('ETHUSDT', '1m', 1592360300000, 1598361300000)[-1])
