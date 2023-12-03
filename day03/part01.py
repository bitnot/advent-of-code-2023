import sys
import re

# TODO: rewrite this

def is_number(c):
    return '0' <= c <= '9'


def is_symbol(c) -> bool:
    return c != '.' and not is_number(c)


def clear_adjacent_numbers(row, col, A):
    min_row = max(0, row - 1)
    max_row = min(len(A)-1, row + 1)
    min_col = max(0, col - 1)
    max_col = min(len(A[0])-1, col + 1)
    for r in range(min_row, max_row + 1):
        for c in range(min_col, max_col + 1):
            if is_number(A[r][c]):
                A[r][c] = '.'
                cl = c-1
                while cl >= 0 and is_number(A[r][cl]):
                    A[r][cl] = '.'
                    cl -= 1
                cr = c+1
                while cr < len(A[0]) and is_number(A[r][cr]):
                    A[r][cr] = '.'
                    cr += 1


def find_non_adjacent(lines) -> [int]:
    A = [list(line.strip()) for line in lines]
    for row in range(len(A)):
        for col in range(len(A[row])):
            if is_symbol(A[row][col]):
                clear_adjacent_numbers(row, col, A)
                A[row][col] = '.'
    #print('\n'.join([''.join(line) for line in A]) + '\n')
    numbers = [int(part)
        for line in A
        for part in ''.join(line).split('.')
        if part
    ]
    return numbers


def find_numbers(lines) -> [int]:
    numbers = []
    for line in lines:
       for num in re.sub(r'[^\d]+', '.', line).split('.'):
           if num:
               numbers.append(int(num))
    return numbers


if __name__ == "__main__":
    lines = sys.stdin.readlines()

    print(sum(find_numbers(lines)) - sum(find_non_adjacent(lines)))
