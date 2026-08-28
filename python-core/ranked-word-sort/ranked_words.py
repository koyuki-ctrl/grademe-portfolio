def sort_ranked_words(words: list[str]) -> list[str]:
    return sorted(words, key=lambda word: (len(word), word.lower()))
