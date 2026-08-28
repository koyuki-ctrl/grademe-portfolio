def sort_ranked_words(words: list[str]) -> list[str]:
    voyelle = "aouiye"
    def compte(words: str) -> int:
        comp = 0
        words = words.lower()
        for a in words:
            if a in voyelle:
                comp += 1
        return comp 
    words = sorted(words, key=compte)
    words = sorted(words, key=lambda el: el.lower())
    words = sorted(words, key=lambda el: len(el))
    return words
["Bee", "ant", "bee", "Ant"]
["Ant", "Bee", "ant", "bee",]
