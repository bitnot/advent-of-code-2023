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
    # Parse input
    neighbours = defaultdict(list)
    start = None
    for i in range(len(pipes)):
        for j in range(len(pipes[0])):
            if pipes[i][j] == '╬':
                start = (i,j)
    
    for i in range(len(pipes)):
        for j in range(len(pipes[0])):
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
    return len(visited) // 2
                

if __name__ == "__main__":
    lines = sys.stdin.readlines()
    cleared = [x.strip() for x in clarify(lines)]
    # print(' ' + ''.join(str(i) for i in range(len(lines[0].strip()))))
    # print("\n".join([str(i) + line for i,line in enumerate(cleared)]))
    pipes = [[x for x in pipe] for pipe in cleared]
    print(solve(pipes))
