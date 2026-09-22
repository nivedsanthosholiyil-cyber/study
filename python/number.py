import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    parts = ip.split(".")
    if len(parts) !=4:
        return False

    for part in parts:
        if not re.fullmatch(r"^\d+$", part):
            return False
        number = int(part)
        if number > 255 or number < 0:
            return False

    return True


if __name__ == "__main__":
    main()