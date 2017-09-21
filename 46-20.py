def translate(original):
    eng2swe = {"merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"år"}
    swedish = []
    for word in original:
        word = word.lower()
        translation = eng2swe.get(word,"not found")
        swedish = swedish + [translation]
    return swedish

english = ["Merry","Christmas","and","happy","New","Year"]
print(translate(english))
