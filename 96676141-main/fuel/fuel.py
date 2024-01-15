from fractions import Fraction

def main():
    user_input = float(get_value("Fraction: "))
    percentage = round(user_input*100)
    if percentage<=1:
        print("E")
    elif percentage>=99:
        print("F")
    else:
        print(f"{percentage}%")


def get_value(prompt):
    while True:
        try:
            fraction = Fraction(input(prompt))

            if fraction.numerator > fraction.denominator:
                raise ValueError

            return fraction

        except (ValueError, ZeroDivisionError):
            pass

main()
