def main():
    Greeting = input("")
    if Greeting[:5].lower() == "hello":
        print("$",0)
    elif Greeting.lower().startswith("h"):
        print("$",20)
    else:
        print("$",100)

main()

