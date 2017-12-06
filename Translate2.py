def translate(original,translation):
    return list(map(lambda x : translation.get(x,"not found"), original))

eng2swe = {"merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"år"}
english = ["merry","christmas","and","happy","new","year"]
print(translate(english,eng2swe))
