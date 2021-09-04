import copy
import sys
from collections import deque

sys.stdin = open("./input.txt", "r")

N, Q = map(int,sys.stdin.readline().split())
NN = pow(2,N)
board = [list(map(int, sys.stdin.readline().split())) for _ in range(NN)]
L = list(map(int, sys.stdin.readline().split()))

dx, dy = (-1,1,0,0),(0,0,-1,1)

print(board)

def count_cluster():
    visited = [[False]*NN for _ in range(NN)]
    cluster = {}
    queue = deque()
    clusters = 1
    sum = 0
    for i in range(NN):
        for j in range(NN):
            sum += board[i][j]
            if not visited[i][j] and board[i][j] > 0: # 방문안했고, 0보다 크다.
                queue.append((i,j))
                while queue:
                    x, y = queue.popleft()
                    if not visited[x][y] and board[x][y] > 0:
                        visited[x][y] = True
                        for d in range(4):
                            nx, ny = x+dx[d], y+dy[d]
                            if nx < 0 or nx >= NN or ny <0 or ny >= NN or board[nx][ny] <= 0: continue
                            queue.append((nx,ny))
                        if board[x][y] > 0:
                            if clusters not in cluster.keys():
                                cluster[clusters] = [(x, y)]
                            else:
                                cluster[clusters].append((x, y))
                clusters+=1
    max_cluster = 0
    for k, c in cluster.items():
        if max_cluster < len(c):
            max_cluster = len(c)
    print(sum)
    print(max_cluster)

def check_board():
    melt_ice = deque()
    for i in range(NN):
        for j in range(NN):
            if board[i][j] > 0: # 방문안했고, 0보다 크다.
                cnt = 0
                for d in range(4):
                    nx, ny = i+dx[d], j+dy[d]
                    if nx < 0 or nx >= NN or ny <0 or ny >= NN or board[nx][ny] <= 0: continue
                    cnt += 1
                if not cnt >= 3:
                    print('meltice : ', i,j, cnt)
                    melt_ice.append((i,j))
    while melt_ice:
        x,y = melt_ice.popleft()
        board[x][y] -= 1

    print('\n=============================================================')
    for _ in board:
        print(_)
    print('=============================================================\n')


def tornado(start, end, region):
    box = deque()
    N = end - start
    for i in range(N):
        box.append(region[start][start + i])
        box.append(region[start + i][end])
        box.append(region[end - i][start])
        box.append(region[end][end - i])
        region[start + i][end] = box.popleft()
        region[end][end - i] = box.popleft()
        region[start][start + i] = box.popleft()
        region[end - i][start] = box.popleft()
    if N > 2:
        return tornado(start + 1, end - 1, region)
    else:
        return region

def firestorm(level):
    grid = pow(2, level)
    print(grid, int(NN/grid), NN)
    box = [[0] * grid for _ in range(grid)]
    for g in range(0, NN, grid):
        print(g)
        for j in range(int(NN/grid)):
            for i in range(grid):
                box[i] = board[g+i][(grid*j):(grid*j)+grid]
            result = tornado(0, grid-1, box)
            for i in range(grid):
                board[g+i][(grid*j):(grid*j)+grid] = result[i]
    check_board()

for level in L:
    firestorm(level)

count_cluster()