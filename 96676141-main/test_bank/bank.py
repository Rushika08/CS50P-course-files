def main():
    user_input = input("Greeting: ")
    print("$",value(user_input),sep="")


def value(greeting):
    lower_Case = greeting.lower()

    trimmed_input = lower_Case.strip()

    if trimmed_input[0:5] == "hello":
        return 0
    elif trimmed_input[0] == "h":
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
