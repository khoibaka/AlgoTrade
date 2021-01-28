from binance.client import Client
from src.const.API_KEY import BINANCE
from src.utils.time_converter import TimeConverter
from src.data.data_converter import list_to_dataframe, list_to_array, string_list_to_number_list
from src.data.io import Save, Load, get_file_name


class BinanceDataFetch:

    def __init__(self):
        self.client = Client(BINANCE['API_KEY'], BINANCE['SECRET_KEY'])
        self.max_entries = 1000000

    def fetch_kline_server(self, symbol, interval, start_time, end_time=None, limit=10000, data_type='json', save_dir=None):
        """Get kline data from Binance
            symbol: 'BTCUSDT', 'ETHUSDT', 'BNBUSDT','BNBBTC', 'ETHBTC', 'LTCBTC'
            interval: 1m, 3m, 5m, 15m, 30m, 1h, 2h, 4h, 6h, 8h, 12h, 1d, 3d, 1w
            start_time: date string
        """
        if not symbol:
            return None

        if limit and limit > self.max_entries:
            limit = self.max_entries

        # Convert start and end time to ms
        start_ms = TimeConverter.date_to_ms(start_time)
        if end_time:
            end_ms = TimeConverter.date_to_ms(end_time)
        else:
            end_ms = None

        output_data = []
        kline_data = string_list_to_number_list(
            self.client.get_klines(
                symbol=symbol,
                interval=interval,
                startTime=start_ms,
                endTime=end_ms,
                limit=limit
            )
        )

        output_data += kline_data
        while (len(kline_data) > 0
               and (not end_ms or kline_data[-1][0] < end_ms)
               and (not limit or len(output_data) < limit)):
            start_ms = kline_data[-1][0] + \
                TimeConverter.interval_to_ms(interval)

            kline_data = string_list_to_number_list(
                self.client.get_klines(
                    symbol=symbol,
                    interval=interval,
                    startTime=start_ms,
                    endTime=end_ms,
                    limit=limit
                )
            )

            output_data += kline_data

        real_start_time = output_data[0][0] if len(output_data) != 0 else 0
        real_end_time = output_data[-1][0] if len(output_data) != 0 else 0

        if limit and limit != 0:
            output_data = output_data[:limit]

        if data_type.lower() == 'csv':
            output_data = list_to_dataframe(output_data)

        elif data_type.lower() == 'array':
            output_data = list_to_array(output_data)

        if save_dir:
            name = get_file_name(
                symbol=symbol,
                interval=interval
            )
            print(name)
            Save.save_file(output_data, save_dir, name)
        return output_data, real_start_time, real_end_time


if __name__ == '__main__':
    bnf = BinanceDataFetch()
    bnf.fetch_kline_server('BTCUSDT', '1h', '08-17-2017', '08-17-2020',
                           None, 'csv', 'F:\Projects\AlgoTradeStorage\CSV')
