import sys
from collections import defaultdict, deque


def clarify(lines):
    for line in lines:
        yield line\
            .replace('F', '╔')\
            .replace('L', '╚')\
            .replace('J', '╝')\
            .replace('7', '╗')\
            .replace('-', '═')\
            .replace('|', '║')\
            .replace('S', '╬')\
            .replace('.', '·')

UP    = (-1, 0)
DOWN  = ( 1, 0)
LEFT  = ( 0,-1)
RIGHT = ( 0, 1)

connections = {
    '╔': (DOWN, RIGHT),
    '╚': (UP,RIGHT),
    '╗': (LEFT,DOWN),
    '╝': (LEFT,UP),
    '═': (LEFT,RIGHT),
    '║': (UP,DOWN)
}

def solve(pipes:[[str]]) -> int:
    height = len(pipes)
    width = len(pipes[0])
    # Parse input
    neighbours = defaultdict(list)
    start = None
    for i in range(height):
        for j in range(width):
            if pipes[i][j] == '╬':
                start = (i,j)
    
    for i in range(height):
        for j in range(width):
            pipe = pipes[i][j]
            if pipe in connections:
                (ai,aj),(bi,bj) = connections[pipe]
                a, b = ((i+ai, j+aj),
                        (i+bi, j+bj))
                neighbours[(i,j)].extend([a,b])
                if a == start:
                   neighbours[a].append((i,j))
                if b == start:
                   neighbours[b].append((i,j))
            
    # Traverse all pipes from the start in both directions
    visited = set()
    q = deque([start])
    while q:
        current = q.popleft()
        visited.add(current)
        for neighbour in neighbours[current]:
            if not neighbour in visited:
                q.append(neighbour)
    # print([len(visited)])
    edge = [(0,j)            for j in range(len(pipes[0]))] \
         + [(len(pipes)-1,j) for j in range(len(pipes[0]))] \
         + [(i,0) for i in range(1,len(pipes)-1)]\
         + [(i,len(pipes[0])-1) for i in range(1,len(pipes)-1)]
    exit_points = set(edge) - visited
    exit_q = deque(exit_points)
    while exit_q:
        current = exit_q.popleft()
        exit_points.add(current)
        for adjacent_point in adjacent_points(current, height-1, width-1):
            if adjacent_point not in visited and adjacent_point not in exit_points:
                exit_q.append(adjacent_point)
    # print(f'exit_points={exit_points}')
    for i in range(height):
        for j in range(width):
            if (i,j) in exit_points:
                pipes[i][j] = '░'
    show(pipes)
    return height*width - len(visited) - len(exit_points)

def adjacent_points(point: (int,int), max_i: int, max_j: int) -> [(int,int)]:
    pi, pj = point
    for i in [-1,0,1]:
        for j in [-1,0,1]:
            if 0 <= pi+i <= max_i and 0 <= pj+j <= max_j and not (i == 0 and j == 0):
                yield pi+i, pj+j
                
def show(pipes):
    print(' ' + ''.join(str(i)[-1] for i in range(len(pipes[0]))))
    print("\n".join([str(i)[-1] + ''.join(str(p) for p in line) for i,line in enumerate(pipes)]))


if __name__ == "__main__":
    lines = sys.stdin.readlines()
    cleared = [x.strip() for x in clarify(lines)]
    pipes = [[x for x in pipe] for pipe in cleared]
    show(pipes)
    print(solve(pipes))
