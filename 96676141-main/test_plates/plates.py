import string
import re

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")



def is_valid(s):
    length = len(s)
    if length<2 or length>6:
        return False

    punct = any(char in string.punctuation or char.isspace() or char == '.' for char in s)
    if punct == True:
        return False

    first_two = s[0:2]
    for letter in first_two:
        if letter.isdigit():
            return False

    for letter in s:
        if letter.isdigit():
            if letter == '0':
                return False
            break

    if s[-1].isalpha():
        for letter in reversed(s[1:-1]):
            if letter.isdigit():
                return False

    for letter in range(len(s)-2):
        if s[letter].isdigit() and s[letter+1].isalpha():
            return False

    return True

if __name__ == "__main__":
    main()
