def bank(greeting):
    """
    Prints value depending on greeting:
    greeting 'hello' -> $0
    greeting starting with 'h' -> $20
    other -> $100
    """
    split_string = greeting.strip().split()
    first_element = split_string[0]

    if first_element == "hello":
        print("$0")
    elif first_element[0] == "h":
        print("$20")
    else:
        print("$100")

greeting = input("Greeting: ").lower()
bank(greeting)
