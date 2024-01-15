import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    pattern = re.compile(r"\b" + re.escape("um") + r"\b", re.IGNORECASE)
    matches = pattern.findall(s)
    return len(matches)


if __name__ == "__main__":
    main()
