import inflect

input_string = []

while True:
    try:
        user_input = input("Name: ")
        input_string.append(user_input)
        if not user_input:
            break

    except (EOFError):
        break

if input_string:
    output = output = inflect.engine().join(input_string, conj="and")
    print("Adieu, adieu, to",output)
