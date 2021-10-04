import sys
from collections import deque

sys.stdin = open('./input.txt', 'r')

dx, dy = (0,0,1,-1), (1,-1,0,0)
N, M, F = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
taxi_sx, taxi_sy = map(int, sys.stdin.readline().split())
p_list = {} # 승객 리스트
taxi = {'fuel': F}

for _ in range(M):
    sx, sy, ex, ey = map(int, sys.stdin.readline().split())
    p_list[(sx-1,sy-1)] = (ex-1, ey-1)
print(p_list)

def take_passenger(same_p):
    visited = [[-1]*N for _ in range(N)]
    q = deque()
    print(same_p)
    same_p.sort()
    px, py, dist = same_p[0]
    taxi['fuel'] -= dist
    if taxi['fuel'] < 0:
        print(-1)
        exit(0)
    q.append((px, py))
    visited[px][py] = 0
    print('this passenger taken. ',same_p[0], dist)
    ex, ey = p_list.pop((px,py)) # 승객 리스트에서 태운 승객 pop
    print('목적지 : ', ex, ey)
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx, ny = x+dx[d], y+dy[d]
            if nx < 0 or ny < 0 or nx >=N or ny >= N or board[nx][ny] == 1: continue
            if visited[nx][ny] == -1:
                q.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1
                if nx == ex and ny == ey: # 승객의 목적지에 도착했을때
                    if taxi['fuel'] - visited[nx][ny] < 0:
                        print(-1)
                        exit(0)
                    taxi['fuel'] = taxi['fuel'] + visited[nx][ny]
                    print('this passenger end. ',taxi['fuel'], visited[nx][ny])
                    return ex, ey
        print("\n ================ visited ==================")
        for v in visited:
            print(v)
        print(" ============================================\n ")
    print(-1)
    exit(0)
def get_passenger(tx, ty):
    visited = [[-1]*N for _ in range(N)]
    q = deque()
    q.append((tx, ty))
    visited[tx][ty] = 0
    dist = -1
    same_p = [] # 거리가 같은 승객 리스트
    if (tx,ty) in p_list.keys(): # 해당 지점에 승객이 있을때.
        if dist == -1:
            dist = visited[tx][ty] #최소거리 세팅
            same_p.append((tx, ty, dist)) # 태우러 갈 승객의 x, y, dist
    while q:
        x, y = q.popleft()
        # 현재 택시 위치 검사
        for d in range(4):
            nx, ny = x+dx[d], y+dy[d]
            if nx<0 or ny < 0 or nx>=N or ny>=N or board[nx][ny] == 1: continue
            if visited[nx][ny] == -1:
                q.append((nx,ny))
                visited[nx][ny] = visited[x][y] + 1
                if (nx,ny) in p_list.keys(): # 해당 지점에 승객이 있을때.
                    if dist == -1: #최소거리 세팅
                        dist = visited[nx][ny]
                    if dist == visited[nx][ny]:
                        same_p.append((nx, ny, visited[nx][ny])) # 태우러 갈 승객의 x, y, dist
                        print('same_p add.',same_p, visited[nx][ny])
                    else: #거리가 더 커졌을 때
                        q.clear()
        # print("\n ================ visited ==================")
        # for v in visited:
        #     print(v)
        # print(" ============================================\n ")
    if not same_p: # 태울 승객이 없을때.
        return -1
    tx, ty = take_passenger(same_p)
    get_passenger(tx,ty)

get_passenger(taxi_sx-1, taxi_sy-1)
print(p_list)
if p_list:
    print(-1)
else: print(taxi['fuel'])