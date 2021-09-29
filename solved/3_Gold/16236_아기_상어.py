import sys
from collections import deque
sys.stdin = open('../../input.txt', 'r')

dx, dy = (-1,0,1,0), (0,-1,0,1)
N = int(sys.stdin.readline())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
shark = {'size': 2, 'ate':0, 'time':0}

def eat_fish(fishes, sx, sy):
    print(fishes)
    fishes.sort()
    print('this fish ate ',fishes[0])
    fx, fy, dist = fishes[0]
    board[fx][fy] = 9 # 상어 이동
    board[sx][sy] = 0  # 상어 이동
    shark['ate'] += 1
    print('\n********************************** ate,', shark['ate'],' size, ', shark['size'])
    if shark['ate'] == shark['size']:
        shark['size'] += 1
        shark['ate'] = 0
        print('\n********************************** size up,', shark['ate'],' size, ', shark['size'])
    shark['time'] += dist
    return fx, fy

def baby_shark_move(loc):
    visited = [[-1]*N for _ in range(N)]
    q = deque()
    q.append(loc)
    visited[loc[0]][loc[1]] = 0
    fish = []
    dist = -1
    while q:
        x,y = q.popleft()
        for d in range(4):
            nx, ny = x+dx[d], y+dy[d]
            if nx < 0 or ny < 0 or nx >= N or ny >= N or board[nx][ny] > shark['size']: continue
            if visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx,ny))
                if board[nx][ny] < shark['size'] and board[nx][ny] != 0: # 물고기가 상어보다 작을때
                    if dist == -1: #최소거리 세팅
                        dist = visited[nx][ny]
                    if dist == visited[nx][ny]:
                        fish.append((nx, ny, visited[nx][ny])) # 먹을 수 있는 물고기의 x, y, dist
                        print(fish, board[nx][ny])
                    else: #거리가 더 커졌을 때
                        q.clear()
        print("\n ================ board ==================")
        for v in board:
            print(v)
        print(" ============================================\n ")

    if not fish: return shark['time']
    fx, fy = eat_fish(fish, loc[0],loc[1])
    baby_shark_move((fx,fy))

for i in range(N):
    for j in range(N):
        if board[i][j] == 9:
            baby_shark_move((i,j))
            print(shark['time'])
            exit(0)