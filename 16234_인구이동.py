import copy
import sys
from collections import deque


sys.stdin = open("./input.txt", "r")

N, L, R = map(int, sys.stdin.readline().split())
dx, dy = (0,-1,0,1),(-1,0,1,0)
hrate = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]

flag = True
pre_unions = {}
move_cnt = 0
while True:
    cnt = 0
    unions = {}
    cnt_unions = {}
    visited = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                union_q = deque()
                union_q.append((i,j))
                visited[i][j] = True
                unions[cnt] = [(i,j)]
                cnt_unions[cnt] = hrate[i][j]
                while union_q:
                    x, y = union_q.popleft()
                    for d in range(4):
                        nx, ny = x + dx[d], y + dy[d]
                        if nx < 0 or nx >= N or ny < 0 or ny >= N or visited[nx][ny]:
                            continue
                        #print(abs(hrate[x][y] - hrate[nx][ny]), L, R)
                        if abs(hrate[x][y] - hrate[nx][ny]) >= L and abs(hrate[x][y] - hrate[nx][ny]) <= R:
                            union_q.append((nx,ny))
                            unions[cnt].append((nx,ny))
                            cnt_unions[cnt] += hrate[nx][ny]
                            visited[nx][ny] = True
                cnt +=1

    if len(pre_unions) == 0:
        pre_unions = copy.deepcopy(unions)
    else:
        print('============ 비교\n',pre_unions,'\n',unions, pre_unions == unions)
        if pre_unions == unions:
            break
        pre_unions = copy.deepcopy(unions)
    cnt_flag = False
    for k,u in unions.items():
        if len(u)>1: # 이동 할 도시 탐색
            avg = cnt_unions[k]/len(u)
            cnt_flag = True
            for city in u:
                hrate[city[0]][city[1]] = int(avg)
    if cnt_flag: move_cnt+=1

    for _ in hrate:
        print(_)
print(move_cnt)
