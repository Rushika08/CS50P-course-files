user_input = input("camelCase: ")

modified_string = ''

for letter in user_input:
    if letter.isupper():
        modified_string += ("_"+letter.lower())
    else:
        modified_string += letter

print(modified_string)



