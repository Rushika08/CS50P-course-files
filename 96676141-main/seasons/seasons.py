from datetime import datetime, date
import re
import sys
import inflect

def main():
    birth_date = input("Date of Birth: ")
    match = re.search(r"^\d\d\d\d-\d\d-\d\d$", birth_date)

    if not match:
        sys.exit("Invalid date")

    reference_date = date.today()
    print(convert(birth_date, reference_date))

def convert(birthday, reference_date):
    today = reference_date
    birthday_m = datetime.strptime(birthday, "%Y-%m-%d").date()

    date_difference = today - birthday_m

    minutes = 1440 * int(date_difference.days)

    p = inflect.engine()
    minutes_words = p.number_to_words(minutes, andword="") + " minutes"

    return minutes_words.capitalize()

if __name__ == "__main__":
    main()
