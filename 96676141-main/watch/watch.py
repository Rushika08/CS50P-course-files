import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    s = s.strip()
    match = re.search(r"^<iframe[^>]*src=\"https?://(?:www\.)?youtube\.com/embed/(\w+)\"[^>]*></iframe>$", s, re.IGNORECASE)
    if match:
        return f"https://youtu.be/{match.group(1)}"
    else:
        return "None"


if __name__ == "__main__":
    main()
