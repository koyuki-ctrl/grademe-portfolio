def shift_letters(text: str, amount: int) -> str:
    result = ""
    for char in text:
        if char.islower():
            result += chr((ord(char) - ord('a') + amount) % 26 + ord('a'))
        elif char.isupper():
            result += chr((ord(char) - ord('A') + amount) % 26 + ord('A'))
        else:
            result += char
    return result