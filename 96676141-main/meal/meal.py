def main():
    user_input = input("What time is it? ")
    user_input = user_input.strip()
    value = convert(user_input)

    if 7<= value <=8:
        print("breakfast time")
    elif 12<= value <=13:
        print("lunch time")
    elif 18<= value <=19:
        print("dinner time")
    else:
        pass


def convert(time):
    parts = time.split(" ")

    mod_time = parts[0].split(":")
    hours = int(mod_time[0])
    minutes = int(mod_time[1])/60

    if len(parts)>1:
        if parts[1] == "p.m.":
            hours = hours + 12

    return hours + minutes

if __name__ == "__main__":
    main()

