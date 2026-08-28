def loose_anagram(left: str, right: str) -> bool:
    # Remove spaces, ignore case, keep everything else
    l = "".join(ch for ch in left.lower() if not ch.isspace())
    r = "".join(ch for ch in right.lower() if not ch.isspace())
    return sorted(l) == sorted(r)