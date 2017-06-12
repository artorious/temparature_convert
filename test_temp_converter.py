import unittest
from temp_converter import convert_celcius_to_fahrenheit

class TempConverterTest(unittest.TestCase):
    # given temp in celcius = correct value in Fahrenheit
    # Data type of input
    # if it throws an exception when data type is incorrect
    # Check for null values

    def test_celcius_is_converted_to_Fahrenheit(self):
        """
            F = C * 9/5 + 32
        """

        actual = convert_celcius_to_fahrenheit(10)
        expected = 50
        self.assertEqual(actual, expected, 
                        'Celcius should convert to correct Fahrenheight')
        self.assertEqual(convert_celcius_to_fahrenheit(20), 68)

        