import pytz
import dateparser
from datetime import datetime


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

        if not isinstance(interval, str) :
            raise ValueError('Interval should be string')

        if len(interval) == 0:
            raise ValueError('Length of interval should be larger than 0')

        unit = interval[-1]
        if not TimeConverter.seconds_per_unit.get(unit):
            raise ValueError('Interval trail should be in these values m,h,d,w')

        try:
            ms = int(interval[:-1])
            ms *= TimeConverter.seconds_per_unit.get(unit) * TimeConverter.ms_per_second
            return ms
        except ValueError:
            raise ValueError('Error with the interval value')

    @staticmethod
    def date_to_ms(date_str):

        if not isinstance(date_str, str):
            raise ValueError('date_str should be string')

        epoch = datetime.utcfromtimestamp(0).replace(tzinfo=pytz.utc)
        d = dateparser.parse(date_str)

        if not d:
            raise ValueError('date_str is not in correct format')

        if d.tzinfo is None or d.tzinfo.utcoffset(d) is None:
            d = d.replace(tzinfo=pytz.utc)

        return int((d - epoch).total_seconds() * TimeConverter.ms_per_second)




if __name__ == '__main__':
    print(TimeConverter.date_to_ms('13-12-2019'))