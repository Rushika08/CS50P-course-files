def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    modified_d = float(d.replace("$",""))
    return modified_d


def percent_to_float(p):
    modified_p = float(p.replace("%",""))
    modified_float = float(modified_p/100)
    return modified_float

main()
