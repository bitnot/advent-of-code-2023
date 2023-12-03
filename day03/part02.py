import sys


def find_adjacent_numbers(row, col, A):
    min_row = max(0, row - 1)
    max_row = min(len(A)-1, row + 1)
    min_col = max(0, col - 1)
    max_col = min(len(A[0])-1, col + 1)
    numbers = []
    for r in range(min_row, max_row + 1):
        c = min_col
        while c <= max_col:
            if A[r][c].isdigit():
                cl = c
                while cl-1 >= 0 and A[r][cl-1].isdigit():
                    cl -= 1
                cr = c
                while cr+1 < len(A[0]) and A[r][cr+1].isdigit():
                    cr += 1
                number = int(''.join(A[r][cl:cr+1]))
                numbers.append(number)
                c = cr
            c += 1
    return numbers


def find_gears(lines) -> [int]:
    A = [list(line.strip()) for line in lines]
    ratios = []
    for row in range(len(A)):
        for col in range(len(A[row])):
            if A[row][col] == '*':
                nums = find_adjacent_numbers(row, col, A)
                if len(nums) == 2:
                    ratios.append(nums[0]*nums[1])
    return ratios


if __name__ == "__main__":
    lines = sys.stdin.readlines()
    print(sum(find_gears(lines)))
