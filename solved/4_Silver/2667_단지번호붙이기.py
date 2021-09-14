import sys
from collections import deque
sys.stdin = open('../../input.txt', 'r')
N = int(sys.stdin.readline())
map = [list(str(sys.stdin.readline().split()[0])) for _ in range(N)]
print(map)
dx, dy = (0,0,1,-1),(1,-1,0,0)
def found_house(map, N):
    danzi = {}
    cnt = 0
    q = deque()
    visited = [[False]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if map[i][j] == '1' and not visited[i][j]:
                q.append((i,j))
                while q:
                    x, y = q.popleft()
                    if not visited[x][y]:
                        if cnt not in danzi.keys():
                            danzi[cnt] = 1
                        else: danzi[cnt] += 1
                        visited[x][y] = True
                        for d in range(4):
                            nx, ny = x+dx[d], y+dy[d]
                            if nx<0 or ny<0 or nx>=N or ny>=N : continue
                            if map[nx][ny] == '1' and not visited[nx][ny]: q.append((nx,ny))
                cnt += 1
    print(len(danzi.keys()))
    result = list(danzi.values())
    result.sort()
    for p in result:
        print(p)
found_house(map, N)