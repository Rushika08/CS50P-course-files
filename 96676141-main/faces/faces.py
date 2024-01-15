def main():
    user_input = input()
    print(convert(user_input))

def convert(input_str):
    modified = input_str.replace(":)","🙂").replace(":(","🙁")
    return modified

main()

