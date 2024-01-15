menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

Total = 0.00

input_strings = []

while True:
    try:
        user_input = input("Item: ").title()
        input_strings.append(user_input)
        if user_input not in menu:
            raise ValueError

        Total += menu[user_input]
        print("Total: ${:.2f}".format(Total),sep="")
    except (ValueError):
        pass
    except (EOFError):
        print("")
        break

