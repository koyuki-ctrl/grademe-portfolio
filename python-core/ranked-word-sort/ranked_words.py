def sort_ranked_words(words: list[str]) -> list[str]:
    vowel = "aeouiy"
    def comp(word: str) -> int:
        count = 0
        for x in word.lower():
            if x in vowel:
                count += 1
        return count
    words = sorted(words, key=comp)
    words = sorted(words, key=lambda tl: tl.lower())
    words = sorted(words, key=lambda le: len(le))
    return words