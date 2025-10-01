def say(number):
    if number < 0 or number > 999_999_999_999:
        raise ValueError("input out of range")
    
    if number == 0:
        return "zero"
    
    ones = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    scales = [(1_000_000_000, "billion"), (1_000_000, "million"), (1_000, "thousand"), (1, "")]

    def say_under_1000(n):
        parts = []

        if n >= 100:
            parts.append(ones[n // 100] + " hundred")
            n %= 100

        if n >= 20:
            parts.append(tens[n // 10] + (f"-{ones[n % 10]}" if n % 10 != 0 else ""))
        elif n > 0:
            parts.append(ones[n])
        elif not parts:
            parts.append(ones[0])

        return " ".join(parts)

    words = []
    for scale_value, scale_name in scales:
        if number >= scale_value:
            group = number // scale_value
            number %= scale_value
            if group > 0:
                words.append(say_under_1000(group))
                if scale_name:
                    words.append(scale_name)

    return " ".join(words)