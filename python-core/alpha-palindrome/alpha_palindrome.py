def is_alpha_palindrome(text: str) -> bool:
    word = "".join([x.lower() for x in text if x.isalpha()])
    return word == word[::-1] if word else False 
