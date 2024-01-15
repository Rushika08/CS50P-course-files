import re
import sys

def main():
    try:
        result = convert(input("Hours: "))
        print(result)
    except ValueError as e:
        print(f"Error: {e}")

def convert(s):
    s = s.strip()
    hour24_1 = 0
    minute24_1 = 0
    hour24_2 = 0
    minute24_2 = 0

    try:
        # checking the input string
        match = re.search(r"^(\d{1,2}(:\d{2})? [APM]{2}) to (\d{1,2}(:\d{2})? [APM]{2})$", s)
        if match:
            # dividing the start and end times
            start_time = match.group(1)
            end_time = match.group(3)

            # checking the time format if ##:## AM/PM
            if re.search(r"^(\d{1,2}(:\d{2}) [APM]{2})$", start_time) and re.search(r"^(\d{1,2}(:\d{2}) [APM]{2})$", end_time):
                time1 = re.split(r'[: ]', start_time)
                time2 = re.split(r'[: ]', end_time)

                if (0 <= int(time1[0]) <= 12):
                    if time1[0] == "12" and time1[2] == "PM":
                        hour24_1 = 12
                    elif time1[0] == "12" and time1[2] == "AM":
                        hour24_1 == 0
                    elif time1[2] == "PM":
                        hour24_1 = int(time1[0]) + 12
                    else:
                        hour24_1 = int(time1[0])
                else:
                    raise ValueError("ValueError")

                if (0 <= int(time1[1]) <= 59):
                    minute24_1 = int(time1[1])
                else:
                    raise ValueError("ValueError")

                if (0 <= int(time2[0]) <= 12):
                    if time2[0] == "12" and time2[2] == "PM":
                        hour24_2 = 12
                    elif time2[0] == "12" and time2[2] == "AM":
                        hour24_2 == 0
                    elif time2[2] == "PM":
                        hour24_2 = int(time2[0]) + 12
                    else:
                        hour24_2 = int(time2[0])
                else:
                    raise ValueError("ValueError")

                if (0 <= int(time2[1]) <= 59):
                    minute24_2 = int(time2[1])
                else:
                    raise ValueError("ValueError")

                return f"{hour24_1:02d}:{minute24_1:02d} to {hour24_2:02d}:{minute24_2:02d}"

            # for the other time format ## AM/PM
            else:
                time1 = start_time.split(" ")
                time2 = end_time.split(" ")

                if (0 <= int(time1[0]) <= 12):
                    if time1[0] == "12" and time1[1] == "PM":
                        hour24_1 = 12
                    elif time1[0] == "12" and time1[1] == "AM":
                        hour24_1 == 0
                    elif time1[1] == "PM":
                        hour24_1 = int(time1[0]) + 12
                    else:
                        hour24_1 = int(time1[0])
                else:
                    raise ValueError("ValueError")


                if (0 <= int(time2[0]) <= 12):
                    if time2[0] == "12" and time2[1] == "PM":
                        hour24_2 = 12
                    elif time2[0] == "12" and time2[1] == "AM":
                        hour24_2 == 0
                    elif time2[1] == "PM":
                        hour24_2 = int(time2[0]) + 12
                    else:
                        hour24_2 = int(time2[0])
                else:
                    raise ValueError("ValueError")

                return f"{hour24_1:02d}:{minute24_1:02d} to {hour24_2:02d}:{minute24_2:02d}"
        else:
            raise ValueError("ValueError")

    except ValueError as e:
        sys.exit(str(e))

if __name__ == "__main__":
    main()
