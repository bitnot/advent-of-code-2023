import sys, math
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

# too slow
# def solve(pattern, directions):
#     paths = [k for k in directions['L'] if k.endswith('A')]
#     jumps = 0
#     for direction in cycle(list(pattern)):
#         jumps += 1
#         if jumps > 1_000_000_000:
#             return -1
#         all_z = True
#         for i, next in enumerate(paths):
#             next = directions[direction][next]
#             paths[i] = next
#             all_z &= next.endswith('Z')
#         if all_z:
#             break
#     return jumps
def factors(n):
    while n > 1:
        for i in range(2, n + 1):
            if n % i == 0:
                n //= i
                yield i
                break

def solve(pattern, directions):
    paths = [k for k in directions['L'] if k.endswith('A')]
    jumps = [0 for _ in paths]

    for i, next in enumerate(paths):
        for direction in cycle(list(pattern)):
            jumps[i] += 1
            next = directions[direction][next]
            paths[i] = next
            if next.endswith('Z'):
                break
    print(jumps)
    unique_factors = set( 
        factor 
        for jump in jumps 
        for factor in factors(jump) 
    )
    return math.prod(unique_factors)

if __name__ == "__main__":
    lines = sys.stdin.readlines()
    pattern = lines[0].strip()
    directions = parse_lines(lines[2:])
    print(solve(pattern, directions))
