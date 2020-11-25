import unittest

from src.compound_interest import CompoundInterest

class CompoundInterestTest(unittest.TestCase):

    # Tests

    # Should return 732.81 given 100 principal, 10 percent, 20 years
    def test_calculate_final_amount__100_10_20(self):
        compound_interest = CompoundInterest(100, 10, 20)
        self.assertEqual(732.81, compound_interest.calculate_final_amount())


    # Should return 181.94 given 100 principal, 6 percent, 10 years
    def test_calculate_final_amount__100_6_10(self):
        compound_interest = CompoundInterest(100, 6, 10)
        self.assertEqual(181.94, compound_interest.calculate_final_amount())


    # Should return 149,058.55 given 100000 principal, 5 percent, 8 years
    def test_calculate_final_amount__100000_5_8(self):
        compound_interest = CompoundInterest(100000, 5, 8)
        self.assertEqual(149058.55, compound_interest.calculate_final_amount())


    # Should return 0.00 given 0 principal, 10 percent, 1 year
    def test_calculate_final_amount__0_10_1(self):
        compound_interest = CompoundInterest(0, 10, 1)
        self.assertEqual(0.00, compound_interest.calculate_final_amount())


    # Should return 100.00 given 100 principal, 0 percent, 10 years
    def test_calculate_final_amount__100_0_10(self):
        compound_interest = CompoundInterest(100, 0, 10)
        self.assertEqual(100.00, compound_interest.calculate_final_amount())

    # Extention tests

    # Should return 118,380.16 given 100 principal, 5 percent, 8 years, 1000 per month
    def test_calculate_final_amount__100_0_10(self):
        compound_interest = CompoundInterest(100, 5, 8)
        self.assertEqual(118380.16, compound_interest.calculate_final_amount_with_contributions(1000))


    # Should return 156,093.99 given 100 principal, 5 percent, 10 years, 1000 per month
    def test_calculate_final_amount__100_5_10_1000(self):
        compound_interest = CompoundInterest(100, 5, 10)
        self.assertEqual(156093.99, compound_interest.calculate_final_amount_with_contributions(1000))


    # Should return 475,442.59 given 116028.86, 7.5 percent, 8 years, 2006 per month
    def test_calculate_final_amount__116028_26_7_5__8_2006(self):
        compound_interest = CompoundInterest(116028.86, 7.5, 8)
        self.assertEqual(475442.59, compound_interest.calculate_final_amount_with_contributions(2006))


    # Should return 718,335.97 given 116028.86 principal, 9 percent, 12 years, 1456 per month
    def test_calculate_final_amount__116028_26_7_5_12_2006(self):
        compound_interest = CompoundInterest(116028.86, 9, 12)
        self.assertEqual(718335.97, compound_interest.calculate_final_amount_with_contributions(1456))


if __name__ == "__main__":
    unittest.main()
