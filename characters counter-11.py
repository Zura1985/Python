name = input("how many symbols are in printed word? ")
if not name:
    print("You must enter a word.")
else:
    counter = len(name)
    print(name, "has", counter, "characters")
