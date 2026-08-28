def convert_base_digits(number: str, source_base: int, target_base: int) -> str:
    base = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    char_list = []

    if source_base < 2 or source_base > 36 or target_base < 2 or target_base > 36:
        return "invalid"

    try:
        decimal_value = int (number, source_base)
    except:
        return "invalid"

    if decimal_value == 0:
        return "0"


    while decimal_value > 0:
        remainder = decimal_value % target_base
        char_list.append(base[remainder])
        decimal_value //= target_base
    return "".join(char_list[::-1])
