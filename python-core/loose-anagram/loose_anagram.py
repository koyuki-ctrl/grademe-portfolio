def loose_anagram(left: str, right: str) -> bool:
    lf = "".join(c for c in left.lower() if not c.isspace())
    rg = "".join(c for c in right.lower() if not c.isspace())
    return sorted(lf) == sorted(rg)