from fractions import Fraction

def main():
    '''
    user_input = float(convert(input("Fraction: ")))
    print(gauge(user_input))
    '''
    try:
        user_input = input("Fraction: ")
        modified = convert(user_input)
        print(gauge(modified))

    except (ValueError,ZeroDivisionError) as e:
        print(f"{e}")



def convert(fraction):
    while True:
        try:
            value = Fraction(fraction)

            if value.numerator > value.denominator:
                raise ValueError

            return round(value*100)

        except ValueError as e1:
            raise ValueError from e1

        except ZeroDivisionError as e2:
            raise ZeroDivisionError from e2


def gauge(percentage):
    if percentage<=1:
        return "E"
    elif percentage>=99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
