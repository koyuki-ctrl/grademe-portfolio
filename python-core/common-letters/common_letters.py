def common_letters(left: str, right: str) -> str:
    result = []
    repeat = []
    r = [x for x in right]
    for l in left:
        if l in r:
            if not l in repeat:
                repeat.append(l) 
                result.append(l)
    return "".join(result)