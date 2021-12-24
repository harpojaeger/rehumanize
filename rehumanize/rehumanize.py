from typing import final


LT_TWENTY = [
    "",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
    "ten",
    "eleven",
    "twelve",
    "thirteen",
    "fourteen",
    "fifteen",
    "sixteen",
    "seventeen",
    "eighteen",
    "nineteen",
]
TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
THOUSANDS = [
    "thousand",
    "million",
    "billion",
    "trillion",
    "quadrillion",
    "quintillion",
    "sextillion",
    "septillion",
    "octillion",
    "nonillion",
    "decillion",
    "undecillion",
    "duodecillion",
    "tredecillion",
    "quattuordecillion",
    "quindecillion",
    "sexdecillion",
    "septendecillion",
    "octodecillion",
    "novemdecillion",
    "vigintillion",
]


def rehumanize(num: int) -> str:
    if num == 0:
        return "zero"
    digits: list[int] = [int(digit) for digit in str(num)]
    written_form: str = ""
    # In this outer loop, we iterate over the input in three-digit groups. Each
    # group's English prefix ("one hundred and fifty" in "one hundred and fifty
    # million", for example) is independent of its place value; it is therefore
    # computed independently before having the "million" appended.
    num_groups: int = 0
    while len(digits) > 0:
        group_value: int = 0

        # This inner loop takes the place of a modulo 1000 operation. For very
        # large numbers, modular arithmetic may have time complexity greater
        # than O(n), and also appears to produce incorrect results.
        tens: int = 0
        while len(digits) > 0 and tens < 3:
            group_value += (10 ** tens) * digits.pop()
            tens += 1

        group_written_form: str = ""
        if group_value > 0:
            # Prepend a separator to the written form of this group _only_ if
            # another group will end up following (i.e. to the left of) it.
            if len(digits) > 0:
                if group_value >= 100 or num_groups > 0:
                    group_written_form = ", "
                else:
                    group_written_form = " and "

            group_written_form += three_digit_prefix(group_value)

            # If this group has a place value greater than 1000, append the
            # written form of the thousands place.
            if num_groups > 0:
                # Numbers greater than 10^66 - 1 require additional prefixes.
                # One vigintillion = 10^63, so one thousand vigintillion =
                # 10^66 and one million viginitillion = 10^69. This allows
                # writing out infinitely large numbers.
                thousands_index: int = (num_groups - 1) % len(THOUSANDS)
                vigintillions: int = int(
                    (num_groups - thousands_index) / len(THOUSANDS)
                )

                group_written_form += " " + THOUSANDS[thousands_index]

                while vigintillions >= 1:
                    group_written_form += " " + THOUSANDS[len(THOUSANDS) - 1]
                    vigintillions -= 1

        written_form = group_written_form + written_form

        num_groups += 1

    return written_form


def three_digit_prefix(num: int) -> str:
    if num < 20:
        return LT_TWENTY[num]

    two_digits: int = num % 100
    hundreds_place: int = int((num - two_digits) / 100)

    # 100 is written "one hundred", not "one hundred and zero", so no need to
    # bother writing out the rest of it.
    if two_digits == 0:
        return f"{LT_TWENTY[hundreds_place]} hundred"

    written_form: str

    if two_digits < 20:
        written_form = LT_TWENTY[two_digits]
    else:
        ones_place: int = two_digits % 10
        tens_place: int = int((two_digits - ones_place) / 10)

        written_form = TENS[tens_place - 2]
        if ones_place > 0:
            written_form += "-" + LT_TWENTY[ones_place]

    if num < 100:
        return written_form

    return f"{LT_TWENTY[hundreds_place]} hundred and {written_form}"
