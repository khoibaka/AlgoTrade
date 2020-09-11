import unittest
from src.utils.time_converter import *

class TimeConverterTest(unittest.TestCase):
    def test_interval_to_ms(self):
        self.assertRaises(ValueError, TimeConverter.interval_to_ms, None)
        self.assertRaises(ValueError, TimeConverter.interval_to_ms, '2')
        self.assertRaises(ValueError, TimeConverter.interval_to_ms, 'w')
        self.assertRaises(ValueError, TimeConverter.interval_to_ms, '2b3w')
        self.assertEqual(TimeConverter.interval_to_ms('2w'), 2 * 60 * 60 * 1000 * 24 * 7)

    def test_date_to_ms(self):
        self.assertRaises(ValueError, TimeConverter.date_to_ms, None)
        self.assertRaises(ValueError, TimeConverter.date_to_ms, '13-13-2019')
        self.assertEqual(TimeConverter.date_to_ms('13-12-2019'), 1576195200000)

    def test_ms_to_date(self):
        print(TimeConverter.ms_to_datetime(1576195200000))
        self.assertEqual(TimeConverter.ms_to_datetime(1576195200000).strftime("%d-%m-%Y"), '13-12-2019')
if __name__ == '__main__':

    unittest.main()
