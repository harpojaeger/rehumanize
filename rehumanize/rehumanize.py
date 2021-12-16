LT_TWENTY = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
             "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
TENS = ["twenty", "thirty", "forty", "fifty",
        "sixty", "seventy", "eighty", "ninety"]
THOUSANDS = ["", "thousand", "million", "billion", "trillion", "quadrillion", "quintillion", "sextillion", "septillion",
             "octillion", "nonillion", "decillion", "undecillion", "duodecillion", "tredecillion", "quattuordecillion", "quindecillion", "sexdecillion", "septendecillion", "octodecillion", "novemdecillion", "vigintillion"]


def rehumanize(num: int) -> str:
    english: str = ""
    if num == 0:
        return "zero"
    # In this outer loop, we will iterate over three-digit chunks of the input.
    # We call each of these a "thousands_group"; its English prefix is
    # independent of how many thousands it represents and can therefore be
    # computed independently.
    thousands_groups: int = 0
    remaining: int = num
    while remaining > 0:
        thousands_group = remaining % 1000
        remaining = int((remaining - thousands_group) / 1000)

        thousands_group_english: str = ""
        if thousands_group > 0:
            if remaining > 0:
                thousands_group_english = ", " if thousands_group > 100 else " and "

            thousands_group_english += process_three_digit_number(
                thousands_group)

        if thousands_groups > 0:
            thousands_group_english += " "

        thousands_group_english += THOUSANDS[thousands_groups]

        english = thousands_group_english + english

        thousands_groups += 1

    return english


def process_three_digit_number(num: int) -> str:
    two_digits: int = num % 100
    english = process_two_digit_number(two_digits)
    quotient = num - two_digits

    if quotient > 0:
        # 100 is written "one hundred", not "one hundred and zero"
        if two_digits == 0:
            english = ""
        else:
            english = f" and {english}"

        hundreds_place: int = int(quotient/100)
        english: str = f"{LT_TWENTY[hundreds_place]} hundred{english}"

    return english


def process_two_digit_number(num: int) -> str:
    if num < 20:
        return LT_TWENTY[num]

    ones_place: int = num % 10
    tens_place: int = int((num - ones_place)/10)

    english: str = TENS[tens_place-2]
    if ones_place > 0:
        english = f"{english}-{LT_TWENTY[ones_place]}"

    return english
