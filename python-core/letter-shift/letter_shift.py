def shift_letters(text: str, amount: int) -> str:
    result = ""
    for ch in text:
        if ch.isupper():
            result += chr((ord(ch) - ord('A') + amount) % 26 + ord('A'))
        elif ch.islower():
            result += chr((ord(ch) - ord('a') + amount) % 26 + ord('a'))
        else:
            result += ch
    return result 