import copy
import sys
from collections import deque

sys.stdin = open("./input.txt", "r")

dx, dy = (1,-1, 0, 0), (0, 0, 1, -1)

N, M = map(int, sys.stdin.readline().split())

lab = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
load = [[-1]*N for _ in range(N)]
for _ in lab:
    print(_)

virus = []

# 바이러스 탐색 및 길 초기화
for i in range(N):
    for j in range(N):
        if lab[i][j] == 2: # 바이러스일때
            virus.append((i,j))

def combination(array, r):
    for i in range(len(array)):
        if r == 1:
            yield [array[i]]
        else:
            for next in combination(array[i+1:], r-1):
                yield [array[i]]+next

min_time = 99999999
isEmpty = 0
for sell in combination(list(range(len(virus))), M):
    # 초기화
    virus_visited = []
    load_to_visit = []
    for i in range(N):
        for j in range(N):
            if lab[i][j] == 2:  # 바이러스일때
                load[i][j] = 0
            elif lab[i][j] == 1:  # 벽일때
                load[i][j] = -1
            else:
                load[i][j] = -2 # 빈칸
                load_to_visit.append(1)
    if len(load_to_visit) == 0:
        print(0)
        sys.exit()
    print(sell)
    active = deque()
    for i in sell:
        active.append(virus[i])
        virus_visited.append(virus[i])
        # load[virus[i][0]][virus[i][1]] = 0
    time = 1
    print('------ Sellected -----', sell)
    for _ in load:
        print(_)
    active_tmp = deque()
    while active:
        print('------ time {0} -----'.format(time))
        x,y = active.popleft()
        for d in range(4):
            nx, ny = x+dx[d], y+dy[d]
            if nx < 0 or ny < 0 or nx >=N or ny >= N: continue
            if load[nx][ny] == -2: #빈공간
                load[nx][ny] = load[x][y] + 1
                load_to_visit.pop()
                active_tmp.append((nx,ny))
            elif load[nx][ny] == 0 and (nx, ny) not in virus_visited: # 새로 발견된 바이러스
                load[nx][ny] = load[x][y] + 1
                active_tmp.append((nx, ny))
                virus_visited.append((nx, ny))
        print(active)
        print(active_tmp)
        if not active:
            if len(load_to_visit) == 0:
                break  # 연구소가 다 바이러스로 채워졌다.
            time += 1
            active.extend(active_tmp)
            active_tmp.clear()

        for _ in load:
            print(_)
    # time = int(max(map(max, load)))

    print( 'Max,,,',time)
    if time < min_time and len(load_to_visit) == 0:
        min_time = time

if min_time != 99999999:
    print(min_time)
else: print(-1)




