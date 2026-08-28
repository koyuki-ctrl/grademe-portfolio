def convert_base_digits(number: str, source_base: int, target_base: int) -> str:
    if source_base < 2 or target_base < 2:
        return "invalid"

    if not number or number[0] == '-':
        return "invalid"

    try:
        decimal_value = int(number, source_base)
    except:
        return "invalid"

    if decimal_value == 0:
        return "0"

    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result_chars = []

    while decimal_value > 0:
        remainder = decimal_value % target_base
        result_chars.append(digits[remainder])
        decimal_value //= target_base
    return "".join(result_chars[::-1])

