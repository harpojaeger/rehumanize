LT_TWENTY = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
             "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
TENS = ["twenty", "thirty", "forty", "fifty",
        "sixty", "seventy", "eighty", "ninety"]
THOUSANDS = ["thousand", "million", "billion"]


def rehumanize(num: int) -> str:
    if num < 20:
        return LT_TWENTY[num]

    ones_place: int = num % 10
    tens_place: int = int((num - ones_place)/10)

    english: str = TENS[tens_place-2]
    if ones_place > 0:
        english = f"{english}-{LT_TWENTY[ones_place]}"

    return english
