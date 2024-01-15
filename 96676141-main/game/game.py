import random

while True:
    try:
        user_input = int(input("Level: "))

        if user_input < 1:
            raise ValueError
        else:
            break

    except ValueError:
        continue


number = random.randint(1, user_input)

while True:
    while True:
        try:
            guess_val = int(input("Guess: "))

            if guess_val < 1:
                raise ValueError
            else:
                break

        except ValueError:
            continue



    if guess_val == number:
        print("Just right!")
        break
    elif guess_val > number:
        print("Too large!")
    else:
        print("Too small!")



