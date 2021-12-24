import unittest

from parameterized import parameterized
from rehumanize import rehumanize


TEST_CASES = [
    (0, "zero"),
    (2, "two"),
    (9, "nine"),
    (10, "ten"),
    (12, "twelve"),
    (20, "twenty"),
    (42, "forty-two"),
    (87, "eighty-seven"),
    (95, "ninety-five"),
    (100, "one hundred"),
    (109, "one hundred and nine"),
    (118, "one hundred and eighteen"),
    (177, "one hundred and seventy-seven"),
    (700, "seven hundred"),
    (999, "nine hundred and ninety-nine"),
    (1000, "one thousand"),
    (1001, "one thousand and one"),
    (1069, "one thousand and sixty-nine"),
    (1512, "one thousand, five hundred and twelve"),
    (42000, "forty-two thousand"),
    (42420, "forty-two thousand, four hundred and twenty"),
    (169420, "one hundred and sixty-nine thousand, four hundred and twenty"),
    (
        5169420,
        "five million, one hundred and sixty-nine thousand, four hundred and twenty",
    ),
    (5000420, "five million, four hundred and twenty"),
    (
        50004735099,
        "fifty billion, four million, seven hundred and thirty-five thousand and ninety-nine",
    ),
    (
        50004735100,
        "fifty billion, four million, seven hundred and thirty-five thousand, one hundred",
    ),
    (69 * (10 ** 33), "sixty-nine decillion"),
    (
        69 * (10 ** 63) + 420 * (10 ** 48),
        "sixty-nine vigintillion, four hundred and twenty quindecillion",
    ),
    (10 ** 66, "one thousand vigintillion"),
    (10 ** 126, "one vigintillion vigintillion"),
    (69 * 10 ** 187, "six hundred and ninety novemdecillion vigintillion vigintillion"),
    (
        12 + 690 * 10 ** 186,
        "six hundred and ninety novemdecillion vigintillion vigintillion and twelve",
    ),
    (50 * 10 ** 189, "fifty vigintillion vigintillion vigintillion"),
]


class RehumanizeTest(unittest.TestCase):

    # Generate test cases whose names end with the expected string value.
    @parameterized.expand(
        [
            (expected_string, int, expected_string)
            for (int, expected_string) in TEST_CASES
        ]
    )
    def test(self, name, num, expected_string):
        self.assertEqual(rehumanize(num), expected_string)


if __name__ == "__main__":
    unittest.main()
