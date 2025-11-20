import unittest
from format_rubles_russian import format_rubles_russian

class TestFormatRublesRussian(unittest.TestCase):
    
    def test_specific_cases(self):
        """Test specific cases with small values and specific kopecks."""
        test_cases = [
            (1.01, "один рубль одна копейка"),
            (2.02, "два рубля две копейки"),
            (3.03, "три рубля три копейки"),
            (4.04, "четыре рубля четыре копейки"),
            (5.05, "пять рублей пять копеек"),
            (11.11, "одиннадцать рублей одиннадцать копеек"),
            (12.12, "двенадцать рублей двенадцать копеек"),
            (21.00, "двадцать один рубль ровно")
        ]
        
        for value, expected in test_cases:
            with self.subTest(value=value):
                self.assertEqual(format_rubles_russian(value), expected)
    
    def test_thousands_with_feminine_forms(self):
        """Test thousands with correct feminine forms."""
        test_cases = [
            (1000.00, "одна тысяча рублей ровно"),
            (2000.00, "две тысячи рублей ровно"),
            (3000.00, "три тысячи рублей ровно"),
            (4000.00, "четыре тысячи рублей ровно"),
            (5000.00, "пять тысяч рублей ровно"),
            (10000.00, "десять тысяч рублей ровно"),
            (21000.00, "двадцать одна тысяча рублей ровно"),
            (1000000.00, "один миллион рублей ровно")
        ]
        
        for value, expected in test_cases:
            with self.subTest(value=value):
                self.assertEqual(format_rubles_russian(value), expected)
    
    def test_large_numbers(self):
        """Test larger values."""
        test_cases = [
            (1000.00, "одна тысяча рублей ровно"),
            (2000.00, "две тысячи рублей ровно"),
            (5000.00, "пять тысяч рублей ровно"),
            (10000.00, "десять тысяч рублей ровно"),
            (15000.00, "пятнадцать тысяч рублей ровно"),
            (20000.00, "двадцать тысяч рублей ровно"),
            (100000.00, "сто тысяч рублей ровно"),
            (500000.00, "пятьсот тысяч рублей ровно"),
            (1000000.00, "один миллион рублей ровно")
        ]
        
        for value, expected in test_cases:
            with self.subTest(value=value):
                self.assertEqual(format_rubles_russian(value), expected)
    
    def test_zero_kopecks(self):
        """Test values with zero kopecks (should show 'ровно')."""
        test_cases = [
            (1.00, "один рубль ровно"),
            (5.00, "пять рублей ровно"),
            (10.00, "десять рублей ровно"),
            (21.00, "двадцать один рубль ровно"),
            (100.00, "сто рублей ровно"),
            (1000.00, "одна тысяча рублей ровно"),
            (5000.00, "пять тысяч рублей ровно"),
            (10000.00, "десять тысяч рублей ровно")
        ]
        
        for value, expected in test_cases:
            with self.subTest(value=value):
                self.assertEqual(format_rubles_russian(value), expected)

if __name__ == '__main__':
    unittest.main()