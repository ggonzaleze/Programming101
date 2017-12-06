words = ["Hello","my","name",3,"Gina"]
lengths = [len(x) for x in words if isinstance(x, str)]
print(lengths)
