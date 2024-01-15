user_input = input("Input: ")

vowels = "AEIOUaeiou"

modified = ""

for letter in user_input:
    if letter not in vowels:
        modified += letter

print("Output: ",modified,sep="")
