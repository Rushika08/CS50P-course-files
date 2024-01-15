user_input = input("What is the answer to the Great Question of Life, the Universe, and Everything? ")

lower_string = user_input.lower()

trimmed_string = lower_string.strip()

if trimmed_string == "42" or trimmed_string == "forty two" or trimmed_string == "forty-two":
    print("Yes")
else:
    print("No")
