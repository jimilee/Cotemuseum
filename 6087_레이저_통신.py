import sys
from collections import deque

sys.stdin = open("./input.txt", "r")
W, H = map(int, sys.stdin.readline().split())
map = [[_ for _ in ''.join(list(sys.stdin.readline().split()))] for _ in range(H)]

dx, dy = (0,0,1,-1), (1,-1,0,0)

def count_mirror(cost, loc):
    path = {0:0,1:0,2:0,3:0}
    cnt = 0

    for i in range(4):
        x,y = loc
        start = cost[x][y]
        while True:
            nx, ny = x+dx[i], y+dy[i]
            if nx < 0 or ny < 0 or nx >=H or ny >= W: break
            if cost[nx][ny] == start-1:
                path[i] += 1
                x, y = nx, ny
                start = cost[nx][ny]
            else:
                break
    print(path)

def laser(loc, map):
    visited = [[False for _ in range(W)] for _ in range(H)]
    cost = [[1 if map[w][h] != '*' else 0 for h in range(W)] for w in range(H)]
    queue = deque()
    queue.append(loc)
    direct = (0,0)
    while queue:
        print()
        x,y = queue.popleft()
        if not visited[x][y]:
            visited[x][y] = True
            print('탐색 노드. ', x, y)
            for i in range(4):
                nx, ny = x+dx[i], y+dy[i]
                if nx < 0 or ny <0 or nx >= H or ny >= W : continue
                if not map[nx][ny] == '*' and not visited[nx][ny]:
                    if map[nx][ny] == 'C':
                        cost[nx][ny] = cost[x][y] + 1
                        print('도착!  \n현재위치 : {0}, 이전위치 : {1}'.format((nx,ny), (x,y)))
                        count_mirror(cost, (x,y))
                        return 0
                    queue.append((nx,ny))
                    cost[nx][ny] = cost[x][y] + 1
                    print('===========================')
                    for p in cost:
                        print(p)
                    for p in visited:
                        print(p)

for i in range(H):
    for j in range(W):
        if map[i][j] == 'C':
            laser((i,j), map)