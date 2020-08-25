


class TimeConverter:
    ms_per_second = 1000
    seconds_per_unit = {
        "m": 60,
        "h": 60 * 60,
        "d": 24 * 60 * 60,
        "w": 7 * 24 * 60 * 60
    }

    @staticmethod
    def interval_to_ms(interval):

        if not isinstance(interval, str) or len(interval) == 0:
            return None

        unit = interval[-1]
        if not TimeConverter.seconds_per_unit.get(unit):
            return None

        try:
            ms = int(interval[:-1])
            ms *= TimeConverter.seconds_per_unit.get(unit) * TimeConverter.ms_per_second
            return ms
        except ValueError:
            return None

def test():
    print(TimeConverter.interval_to_ms('2w'))

if __name__ == '__main__':
    test()