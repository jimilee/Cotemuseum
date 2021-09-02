import sys
from collections import deque
sys.stdin = open("../../input.txt", "r")

N = int(sys.stdin.readline())
K = int(sys.stdin.readline())
apples = [list(map(int, sys.stdin.readline().split())) for _ in range(K)]
L = int(sys.stdin.readline())
move = {}
for _ in range(L):
    X, C = map(str, sys.stdin.readline().split())
    move[X] = C

snake = deque()
snake.append((0,0))
dx,dy = (0,1,0,-1),(1,0,-1,0)

def move_snake():
    d_s = 0
    time = 0
    while snake:
        if str(time) in move.keys():
            if move[str(time)] == 'L':
                d_s = 3 if d_s == 0 else d_s-1
            else:
                d_s = 0 if d_s == 3 else d_s+1
        x,y = snake.pop()
        time += 1
        nx, ny = x+dx[d_s], y+dy[d_s]

        if [nx+1,ny+1] in apples:
            apples.remove([nx+1,ny+1])
            snake.append((x,y))
            snake.append((nx,ny))
        elif (nx,ny) in snake or nx < 0 or ny <0 or nx >= N or ny >= N:
            return time
        else:
            snake.append((x,y))
            snake.append((nx,ny))
            snake.popleft()

print(move_snake())


