import sys
from collections import deque

sys.stdin = open("./input.txt", "r")

N, M = map(int, sys.stdin.readline().split())

A = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

directions = [(-1,0),(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1)]

cloud_loc = deque([(N-1,0),(N-1,1),(N-2,0),(N-2,1)])

def move_cloud(d, s, wasCloud):
    sx, sy = (directions[d-1][1]*s), (directions[d-1][0]*s)
    num_of_cloud = len(cloud_loc)
    for loc in range(num_of_cloud):
        x,y = cloud_loc.popleft()
        nx, ny = (x+sx+N)%N, (y+sy+N)%N
        A[nx][ny] += 1
        wasCloud[nx][ny] = True
        cloud_loc.append((nx,ny))
    return wasCloud

def check_basket(): #구름 대각선방향 체크 , 물 복사 마법
    num_of_cloud = len(cloud_loc)
    for loc in range(num_of_cloud):
        x, y = cloud_loc.popleft()
        for d in range(1,8,2):
            nx, ny = x + directions[d][1], y + directions[d][0]
            if nx<0 or ny<0 or nx>N-1 or ny>N-1:
                continue
            if A[nx][ny]>0:
                A[x][y] += 1
        cloud_loc.append((x,y))

def make_cloud(wasCloud):
    new_cloud = deque()
    for x in range(N):
        for y in range(N):
            if A[x][y] >= 2 and not wasCloud[x][y]:
                new_cloud.append((x,y))
                wasCloud[x][y] = True
                A[x][y] -= 2
    cloud_loc.clear()
    cloud_loc.extend(new_cloud)

for _ in range(M):
    wasCloud = [[False] * N for _ in range(N)]
    d, s = map(int, sys.stdin.readline().split())
    wasCloud = move_cloud(d,s, wasCloud)
    check_basket()
    make_cloud(wasCloud)

total = 0
for x in A:
    for w in x:
        total += int(w)
print(total)
