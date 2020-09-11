import json
import pandas as pd
import os


class Save:
    @staticmethod
    def save_file(data, path, name):
        if isinstance(data, pd.DataFrame):
            data.to_csv(os.path.join(path, name + '.csv'))
        elif isinstance(data, list):
            with open(os.path.join(path, name + '.json'), 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)

    @staticmethod
    def get_file_name(symbol, start_time, end_time, interval):
        start_time = start_time.strftime("%m-%d-%y")
        end_time = end_time.strftime("%m-%d-%y")
        return "{}_{}_{}_{}".format(symbol, start_time, end_time, interval)

class Load:
    @staticmethod
    def load_file(file_path):
        file_name, ext = os.path.splitext(file_path)
        if ext == '.csv':
            df = pd.read_csv(file_path, index_col=0)
            return df


if __name__ == '__main__':
    df =Load.load_file('F:\Projects\AlgoTradeStorage\CSV\BNBUSDT_11-06-17_08-17-20_1d.csv')
