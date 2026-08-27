def count_digit_steps(text: str) -> int:
    count = 0
    for i in range(len(text) - 1):
        if (
            (text[i].isdigit() and text[i + 1].isdigit())
            and (int(text[i]) + 1 == int(text[i + 1]))
        ):
            count += 1
    return count