LT_TWENTY = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
             "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
TENS = ["twenty", "thirty", "forty", "fifty",
        "sixty", "seventy", "eighty", "ninety"]
THOUSANDS = ["thousand", "million", "billion", "trillion", "quadrillion", "quintillion", "sextillion", "septillion",
             "octillion", "nonillion", "decillion", "undecillion", "duodecillion", "tredecillion", "quattuordecillion", "quindecillion", "sexdecillion", "septendecillion", "octodecillion", "novemdecillion", "vigintillion"]


def rehumanize(num: int) -> str:
    if num == 0:
        return "zero"
    digits: list[int] = [int(digit) for digit in str(num)]
    written_form: str = ""
    # In this outer loop, we will iterate over the input in three-digit groups.
    # Each group's English prefix ("one hundred and fifty" in "one hundred and
    # fifty million", for example) is independent of its place value; it is
    #  therefore computed independently before having the name appended.
    num_groups: int = 0
    while len(digits) > 0:
        group_value: int = 0

        # This inner loop takes the place of a modulo 1000 operation. For very
        # large numbers, modular arithmetic may have time complexity greater
        # than O(n), and also appears to produce incorrect results.
        tens: int = 0
        while len(digits) > 0 and tens < 3:
            group_value += ((10**tens) * digits.pop())
            tens += 1

        group_written_form: str = ""
        if group_value > 0:
            # Prepend a separator to the written form of this group _only_ if
            # another group will end up following it.
            if len(digits) > 0:
                if group_value >= 100 or num_groups > 0:
                    group_written_form = ", "
                else:
                    group_written_form = " and "

            group_written_form += process_three_digit_number(group_value)

            if num_groups > 0:
                group_written_form += " " + THOUSANDS[num_groups-1]

        written_form = group_written_form + written_form

        num_groups += 1

    return written_form


def process_three_digit_number(num: int) -> str:
    two_digits: int = num % 100
    written_form = process_two_digit_number(two_digits)
    if num < 100:
        return written_form

    # 100 is written "one hundred", not "one hundred and zero"
    if two_digits == 0:
        written_form = ""
    else:
        written_form = f" and {written_form}"

    hundreds_place: int = int((num - two_digits)/100)
    written_form: str = f"{LT_TWENTY[hundreds_place]} hundred{written_form}"

    return written_form


def process_two_digit_number(num: int) -> str:
    if num < 20:
        return LT_TWENTY[num]

    ones_place: int = num % 10
    tens_place: int = int((num - ones_place)/10)

    written_form: str = TENS[tens_place-2]
    if ones_place > 0:
        written_form += "-" + LT_TWENTY[ones_place]

    return written_form
