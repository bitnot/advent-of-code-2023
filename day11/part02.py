import sys
from itertools import combinations

def show(points: [[str]]):
    print(' ' + ''.join(str(i)[-1] for i in range(len(points[0]))))
    print("\n".join([str(i)[-1] + ''.join(str(c) for c in line) for i,line in enumerate(points)]))


def debug_pairs(pairs, expanded):
    print(f'found {len(pairs)} pairs')
    for pair in pairs:
        ((row_a, col_a),(row_b,col_b)) = pair
        number_a = expanded[row_a][col_a]
        number_b = expanded[row_b][col_b]
        print(f"distance_between({number_a},{number_b}) = {distance_between((row_a, col_a),(row_b,col_b))} \t# {pair}")



def find_empty_rows(points: [[str]]) -> [int]:
    empty_line_ids = []
    for i, line in enumerate(points):
        if all('.' == c for c in line):
            empty_line_ids.append(i)
    return empty_line_ids

def transpose(matrix):
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]

def find_empty_cols(points: [[str]]) -> [int]:
    return find_empty_rows(transpose(points))


def distance_between(
    galaxy_a: (int,int), 
    galaxy_b: (int,int),
    empty_row_count,
    empty_col_count,
    multiplier) -> int:
    ((row_a, col_a),(row_b,col_b)) = (galaxy_a, galaxy_b)

    row_a, row_b = sorted([row_a, row_b])
    col_a, col_b = sorted([col_a, col_b])

    return (row_b - row_a) + (col_b-col_a) \
        + (empty_row_count[row_a][row_b] + empty_col_count[col_a][col_b])*(multiplier -1)

def precompute_empty_count(empty_ids, N):
    empty_count = [[0 for _ in range(N)] for _ in range(N)]
    for source in range(N-1):
        if source in empty_ids:
            empty_count[source][source] = 1

        for destination in range(source+1,N):
            empty_count[source][destination] = empty_count[source][destination-1] + int(destination in empty_ids)
    return empty_count

def solve(lines: [str], multiplier):
    points =[[c for c in line.strip()]
        for line in lines
    ]
    # show(points)
    empty_row_ids = set(find_empty_rows(points))
    empty_col_ids = set(find_empty_cols(points))


    # show(expanded)
    galaxies = []
    galaxy_number = 0
    for row in range(len(points)):
        for col in range(len(points[0])):
            if points[row][col] == '#':
                galaxies.append((row,col))
                galaxy_number += 1
                points[row][col] = str(galaxy_number)
    show(points)

    pairs = list(combinations(galaxies, 2))
    # debug_pairs(pairs, points)

    empty_row_count = precompute_empty_count(empty_row_ids, len(points))
    empty_col_count = precompute_empty_count(empty_col_ids, len(points[0]))
    
    # print(f"empty_col_ids={empty_col_ids}")
    # print("empty_col_count")
    # show(empty_col_count)

    def distance(a,b):
        return distance_between(a,b, empty_row_count, empty_col_count, multiplier)

    distances = [
        distance(a,b) for (a,b) in pairs
    ]
    print(sum(distances))
    

if __name__ == "__main__":
    lines = sys.stdin.readlines()
    multiplier = 1000000
    solve(lines, multiplier)
