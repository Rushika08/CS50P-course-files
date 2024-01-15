input_strings = {}

while True:
    try:
        user_input = input().upper()
        if not user_input:
            break
        input_strings[user_input] = input_strings.get(user_input, 0) + 1

    except (EOFError):
        break

for item, count in sorted(input_strings.items()):
    print(f"{count} {item.upper()}")
