from src.const.kline_const import  SYMBOLS, INTERVALS
from src.data.fetch import BinanceDataFetch
def fetch_all():
    bnf = BinanceDataFetch()
    for symbol in SYMBOLS:
        for interval in INTERVALS:
            bnf.fetch_kline(symbol, interval, '08-17-2017', '08-17-2020', None, 'csv',
                            'F:\Projects\AlgoTradeStorage\CSV')

if __name__ == '__main__':
    fetch_all()