import sys
import os

def is_comment(line_state):
    return line_state.strip().startswith("# ")

def is_whiteSpace(line_state):
    return not line_state.strip()

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
else:
    file_path = sys.argv[1]
    if not os.path.exists(file_path):
        sys.exit("File does not exist")

    if not file_path.lower().endswith(".py"):
        sys.exit("Not a python file")

    try:
        count = 0
        with open(sys.argv[1], "r") as file:
            for line in file:
                if not is_comment(line) and not is_whiteSpace(line):
                    count +=1
                else:
                    pass
        print(count)
    except FileNotFoundError:
        pass

