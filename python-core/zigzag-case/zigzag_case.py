def zigzag_letters(text: str) -> str:
    result = []
    letter_count = 0
    for ch in text:
        if ch.isalpha():
            if letter_count % 2 == 0:
                result.append(ch.lower())
            else:
                result.append(ch.upper())
            letter_count += 1
        else:
            result.append(ch)
    return ''.join(result)