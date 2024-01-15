from datetime import datetime

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    user_input = input("Date: ").strip()

    try:
        date_object = datetime.strptime(user_input, "%B %d, %Y")

        if date_object.strftime("%B") not in months:
            raise ValueError

    except ValueError:
        try:
            date_object = datetime.strptime(user_input, "%m/%d/%Y")
        except ValueError:
            try:
                date_object = datetime.strptime(user_input, "%Y-%m-%d")
            except ValueError:
                continue
    break

print(date_object.strftime("%Y-%m-%d"))
