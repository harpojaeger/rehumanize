LT_TWENTY = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
             "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
TENS = ["twenty", "thirty", "forty", "fifty",
        "sixty", "seventy", "eighty", "ninety"]
THOUSANDS = ["thousand", "million", "billion"]


def rehumanize(num: int) -> str:
    if num < 20:
        return LT_TWENTY[num]
