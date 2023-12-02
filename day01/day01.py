import sys


def calibrate(value):
    digits = [ord(c) - ord('0') for c in value if '0' <= c <= '9']
    if not digits:
        return 0
    return 10*digits[0] + digits[-1]

if __name__ == "__main__":
    lines = sys.stdin.readlines()
    print(sum(calibrate(line) for line in lines))
