def delimiters_balanced(text: str) -> bool:
    brakets = {')':'(', '}':'{', ']':'['}
    stack = []
    for char in text:
        if char in '({[':
            stack.append(char)
        elif char in ')}]':
            if not stack or stack.pop() != brakets[char]:
                return False
    return len(stack) == 0
