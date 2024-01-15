user_input = input("Greeting: ")

lower_Case = user_input.lower()

trimmed_input = lower_Case.strip()

if trimmed_input[0:5] == "hello":
    print("$0")
elif trimmed_input[0] == "h":
    print("$20")
else:
    print("$100")
