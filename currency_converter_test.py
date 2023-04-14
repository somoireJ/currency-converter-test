import unittest

def convert_currency(amount, exchange_rate):
    """Convert a currency amount using the specified exchange rate."""
    return amount * exchange_rate

class TestCurrencyConverter(unittest.TestCase):
    def test_convert_currency(self):
        # test conversion from USD to EUR
        self.assertEqual(convert_currency(100, 0.83), 83)
        self.assertEqual(convert_currency(50, 0.83), 41.5)
        self.assertEqual(convert_currency(0, 0.83), 0)
        
        # test conversion from USD to GBP
        self.assertEqual(convert_currency(100, 0.72), 72)
        self.assertEqual(convert_currency(50, 0.72), 36)
        self.assertEqual(convert_currency(0, 0.72), 0)
        
        # test conversion from EUR to GBP
        self.assertEqual(convert_currency(100, 0.87), 87)
        self.assertEqual(convert_currency(50, 0.87), 43.5)
        self.assertEqual(convert_currency(0, 0.87), 0)

if __name__ == '__main__':
    unittest.main()
    print("Tests complete.")
