import sys

words = {
    "one":      1,
    "two":      2,
    "three":    3,
    "four":     4,
    "five":     5,
    "six":      6,
    "seven":    7,
    "eight":    8,
    "nine":     9
}

def calibrate(value):
    digits = []
    while value:
        if '0' <= value[0] <= "9":
            digits.append(ord(value[0]) - ord('0'))
        else:
            for word, digit in words.items():
                if value.startswith(word):
                    digits.append(digit)
        value = value[1:]
    if not digits:
        return 0
    return 10*digits[0] + digits[-1]

if __name__ == "__main__":
    lines = sys.stdin.readlines()
    print(sum(calibrate(line) for line in lines))
