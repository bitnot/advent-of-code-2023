import sys
from itertools import combinations

def show(points: [[str]]):
    print(' ' + ''.join(str(i)[-1] for i in range(len(points[0]))))
    print("\n".join([str(i)[-1] + ''.join(c for c in line) for i,line in enumerate(points)]))


def expand_rows(points: [[str]]) -> [[str]]:
    """Duplicates "empty" rows (not columns)"""
    points = points[:]
    empty_line_ids = []
    for i, line in enumerate(points):
        if all('.' == c for c in line):
            empty_line_ids.append(i)
    empty_line = ['.' for _ in points[0]]
    for i in reversed(empty_line_ids):
        points.insert(i, empty_line)
    return points

def expand(points: [[str]]) -> [[str]]:
    """Duplicates empty rows and columns"""
    return transpose(expand_rows(transpose(expand_rows(points))))

def transpose(matrix):
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]

def distance_between(galaxy_a: (int,int), galaxy_b: (int,int)) -> int:
    ((row_a, col_a),(row_b,col_b)) = (galaxy_a, galaxy_b)
    return abs(row_a - row_b)+abs(col_a-col_b) 

def debug_pairs(pairs, expanded):
    print(f'found {len(pairs)} pairs')
    for pair in pairs:
        ((row_a, col_a),(row_b,col_b)) = pair
        number_a = expanded[row_a][col_a]
        number_b = expanded[row_b][col_b]
        print(f"distance_between({number_a},{number_b}) = {distance_between((row_a, col_a),(row_b,col_b))} \t# {pair}")

def solve(lines: [str]):
    points =[[c for c in line.strip()]
        for line in lines
    ]
    # show(points)
    expanded = expand(points)
    # show(expanded)
    galaxies = []
    galaxy_number = 0
    for row in range(len(expanded)):
        for col in range(len(expanded[0])):
            if expanded[row][col] == '#':
                galaxies.append((row,col))
                galaxy_number += 1
                expanded[row][col] = str(galaxy_number)
    show(expanded)

    pairs = list(combinations(galaxies, 2))
    # debug_pairs(pairs, expanded)

    distances = [
        distance_between(a,b) for (a,b) in pairs
    ]
    print(sum(distances))
    

if __name__ == "__main__":
    lines = sys.stdin.readlines()
    solve(lines)
