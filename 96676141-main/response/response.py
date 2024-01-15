import validators

def validate_email(email):
    if validators.email(email):
        print("Valid")
    else:
        print("Invalid")

def main():
    user_email = input("What's your email address? ")
    validate_email(user_email)

if __name__ == "__main__":
    main()
