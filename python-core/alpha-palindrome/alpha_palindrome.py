def is_alpha_palindrome(text: str) -> bool:
    clean_text = "".join([txt.lower() for txt in text if txt.isalpha()])
    return clean_text[::-1] == clean_text if clean_text else False