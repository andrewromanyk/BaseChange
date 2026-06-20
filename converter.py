import math

DIGIT_TO_CHAR = {
    "0": "0",
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9",
    "10": "A",
    "11": "B",
    "12": "C",
    "13": "D",
    "14": "E",
    "15": "F",
    "16": "G",
    "17": "H",
    "18": "I",
    "19": "J",
    "20": "K",
    "21": "L",
    "22": "M",
    "23": "N",
    "24": "O",
    "25": "P",
    "26": "Q",
    "27": "R",
    "28": "S",
    "29": "T",
    "30": "U",
    "31": "V",
    "32": "W",
    "33": "X",
    "34": "Y",
    "35": "Z",
}

CHAR_TO_DIGIT = {v: k for k, v in DIGIT_TO_CHAR.items()}

sign = ""


def is_valid(source_base, number_string):
    if number_string.startswith("-"):
        number_without_sign = number_string[1:]
    else:
        number_without_sign = number_string

    for character in number_without_sign:
        if character != "." and int(CHAR_TO_DIGIT[character]) >= source_base:
            print(f"Number {number_string} is not part of base {source_base} system")
            return False
    return True


def to_decimal(source_base, number_string):
    parts = number_string.split(".")

    if number_string.startswith("-"):
        integer_part = parts[0][1:]
        global sign
        sign = "-"
    else:
        integer_part = parts[0]

    if len(parts) != 1:
        fractional_part = parts[1]
        if len(fractional_part) > 3:
            print("Fractional part must have at most 3 digits after the decimal point")
            return None
    else:
        fractional_part = 0

    if source_base == 10:
        return float(number_string)

    decimal_value = 0

    for i in range(len(integer_part)):
        decimal_value += int(CHAR_TO_DIGIT[integer_part[i]]) * (source_base ** (len(integer_part) - i - 1))

    if fractional_part != 0:
        for i in range(len(fractional_part)):
            decimal_value += float(CHAR_TO_DIGIT[fractional_part[i]]) * (source_base ** (-1 - i))

    return decimal_value


def convert_base(source_base, number_string, target_base):
    if target_base == 10:
        return sign + str(to_decimal(source_base, number_string))

    if source_base == target_base:
        return number_string

    decimal_value = to_decimal(source_base, number_string)

    integer_part = math.floor(decimal_value)
    if integer_part != decimal_value:
        fractional_str = str(decimal_value)[len(str(integer_part)) + 1:]
        fractional_part = float(fractional_str) / (10 ** len(fractional_str))
    else:
        fractional_part = 0

    result_digits = []
    while True:
        if integer_part >= target_base:
            result_digits.append(DIGIT_TO_CHAR[str(int(integer_part % target_base))])
            integer_part = integer_part // target_base
        else:
            result_digits.append(DIGIT_TO_CHAR[str(integer_part)])
            break

    result = sign + "".join(result_digits[::-1])

    if fractional_part != 0:
        fractional_digits = []
        for i in range(len(str(fractional_part))):
            fractional_part = fractional_part * target_base
            floor_value = math.floor(fractional_part)
            fractional_digits.append(DIGIT_TO_CHAR[str(floor_value)])
            fractional_part = fractional_part - floor_value
        result += "." + "".join(fractional_digits)

    return result


conversion_valid = False

try:
    source_base = int(input("Enter source base (2-36): "))
except Exception:
    print("Invalid numeric input")
else:
    if source_base > 36 or source_base < 2:
        print("Base must be between 2 and 36")
    else:
        conversion_valid = True

if conversion_valid:
    number_to_convert = input("Enter the number (use . for decimal point): ")
    try:
        if is_valid(source_base, number_to_convert):
            if to_decimal(source_base, number_to_convert) >= 10 ** 9:
                print("Number value is too large")
                conversion_valid = False
            else:
                number_to_convert = str(number_to_convert)
        else:
            conversion_valid = False
    except Exception:
        print("Invalid numeric input")
        conversion_valid = False

if conversion_valid:
    try:
        target_base = int(input("Enter target base (2-36): "))
    except Exception:
        print("Invalid numeric input")
        conversion_valid = False
    else:
        if target_base > 36 or target_base < 2:
            print("Base must be between 2 and 36")
            conversion_valid = False
        else:
            conversion_valid = True

if conversion_valid and is_valid(source_base, number_to_convert):
    print(convert_base(source_base, number_to_convert, target_base))
