def main():
    user_input = input("Input: ")
    print(shorten(user_input))

def shorten(word):
    vowels = "AEIOUaeiou"

    modified = ""

    for letter in word:
        if letter not in vowels:
            modified += letter

    return modified

if __name__ == "__main__":
    main()
