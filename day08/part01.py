import sys
from itertools import cycle


def parse_lines(lines):
    left_child = {}
    right_child = {}
    for line in lines:
        parent, rest = line.strip().split("=")
        parent = parent.strip()
        left, right = rest.strip()[1:-1].split(",")
        left_child[parent] = left.strip()
        right_child[parent] = right.strip()
    directions = {
        'L': left_child,
        'R': right_child
    }
    return directions

def solve(pattern, directions):
    next = 'AAA'
    jumps = 0
    for direction in cycle(list(pattern)):
        next = directions[direction][next]
        jumps += 1
        if next == 'ZZZ':
            return jumps
        if jumps > 1_000_000:
            break
    return -1


if __name__ == "__main__":
    lines = sys.stdin.readlines()
    pattern = lines[0].strip()
    directions = parse_lines(lines[2:])
    print(solve(pattern, directions))
