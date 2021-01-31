from src.statistics.moving_average import MovingAverage

STATISTICS = {
    'Moving Average': MovingAverage
}


class Factory:

    @staticmethod
    def get_statistics(statistics_name, *args, **kwargs):
        return STATISTICS.get(statistics_name)(**kwargs)


if __name__ == '__main__':
    print(Factory.get_statistics('Moving Average', window=3).get_name())
