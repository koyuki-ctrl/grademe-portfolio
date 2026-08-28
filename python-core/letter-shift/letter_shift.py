def shift_letters(text: str, amount: int) -> str:
    result = ""
    for ch in text:
        if ch.islower():
            result = result + chr((ord(ch) - ord('a') + amount) % 26 + ord('a'))
        elif ch.isupper(): 
            result = result + chr((ord(ch) - ord('A') + amount) % 26 + ord('A'))
        else:
            result = result + ch
    return result 