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
    '║': (UP,DOWN),
    '╬': (UP,DOWN,LEFT,RIGHT)
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
            if pipe != '╬' and pipe in connections:
                for (ai,aj) in connections[pipe]:
                    a = (i+ai, j+aj)
                    neighbours[(i,j)].append(a)
                    if a == start:
                        neighbours[a].append((i,j))
            
    # Traverse all pipes from the start in both directions
    visited = set()
    q = deque([start])
    while q:
        current = q.popleft()
        visited.add(current)
        for neighbour in neighbours[current]:
            if not neighbour in visited:
                q.append(neighbour)
    #####
    zoomed = [['.' for _ in range(width*3)] for _ in range(height*3)]
    zoomed_visited = set()
    for i in range(height):
        for j in range(width):
            if (i,j) in visited:
                #center_zoomed
                zoomed[i*3+1][j*3+1] = pipes[i][j]
                zoomed_visited.add((i*3+1,j*3+1))

                for connection in connections[pipes[i][j]]:
                    if connection == UP:
                        zoomed[i*3][j*3+1] = '║'
                        zoomed_visited.add((i*3,j*3+1))
                    elif connection == DOWN:
                        zoomed[i*3+2][j*3+1] = '║'
                        zoomed_visited.add((i*3+2,j*3+1))
                    elif connection == LEFT:
                        zoomed[i*3+1][j*3] = '═'
                        zoomed_visited.add((i*3+1,j*3))
                    else: #RIGHT
                        zoomed[i*3+1][j*3+2] = '═'
                        zoomed_visited.add((i*3+1,j*3+2))
    # print(f'len(zoomed_visited)={len(zoomed_visited)}')

    # Fill edge in zoomed
    edge = [(0,j)            for j in range(width*3)] \
         + [(height*3-1,j)   for j in range(width*3)] \
         + [(i,0)            for i in range(1,height*3-1)]\
         + [(i,width*3-1)    for i in range(1,height*3-1)]
    zoomed_outer = set(edge) - zoomed_visited
    # print(f'len(zoomed_outer)={len(zoomed_outer)}; len(zoomed_visited)={len(zoomed_visited)}; size(zoomed)={height*width*9}')
    exit_q = deque(zoomed_outer)
    queued = zoomed_outer.copy()
    while exit_q:
        current = exit_q.popleft()
        zoomed_outer.add(current)
        for adjacent_point in adjacent_points(current, height*3-1, width*3-1):
            if      adjacent_point not in queued \
                and adjacent_point not in zoomed_visited \
                and adjacent_point not in zoomed_outer:
                exit_q.append(adjacent_point)
                queued.add(adjacent_point)
    # print(f'len(zoomed_outer)={len(zoomed_outer)}')
    outer_count = 0
    for i in range(height):
        for j in range(width):
            if (i*3+1,j*3+1) in zoomed_outer:
                pipes[i][j] = '░'
                outer_count += 1
    show(pipes)
    #
    return height*width - len(visited) - outer_count

def adjacent_points(point: (int,int), max_i: int, max_j: int) -> [(int,int)]:
    pi, pj = point
    for i in [-1,0,1]:
        for j in [-1,0,1]:
            if 0 <= pi+i <= max_i and 0 <= pj+j <= max_j and not (i == j == 0):
                yield pi+i, pj+j
                
def show(pipes):
    print(' ' + ''.join(str(i)[-1] for i in range(len(pipes[0]))))
    print("\n".join([str(i)[-1] + ''.join(str(p) for p in line) for i,line in enumerate(pipes)]))


if __name__ == "__main__":
    lines = sys.stdin.readlines()
    cleared = [x.strip() for x in clarify(lines)]
    pipes = [[x for x in pipe] for pipe in cleared]
    # show(pipes)
    print(solve(pipes))
