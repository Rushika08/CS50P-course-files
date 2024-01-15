import random

def main():
    score = 0
    input_level = get_level()
    for j in range(10):
        x = generate_integer(input_level)
        y = generate_integer(input_level)

        for i in range(3):
            try:
                answer = int(input(f"{x} + {y} = "))
                if answer != (x+y):
                    print("EEE")
                    if i == 2:
                        print(f"{x} + {y} = {x+y}")
                else:
                    score += 1
                    break
            except ValueError:
                print("EEE")
                if i == 2:
                        print(f"{x} + {y} = {x+y}")
                continue

        if j==9:
            print(f"Score: {score}")

def get_level():
    while True:
        try:
            user_input = int(input("Level: "))
            if user_input < 1 or user_input > 3:
                raise ValueError
            else:
                break
        except ValueError:
            continue
    return user_input


def generate_integer(level):
    if level == 1:
        lower_bound = 0
        upper_bound = 10
    else:
        lower_bound = 10 ** (level-1)
        upper_bound = 10 ** level
    return random.randrange(lower_bound, upper_bound, 1)


if __name__ == "__main__":
    main()
