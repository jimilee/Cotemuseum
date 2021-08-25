import sys
from collections import deque

#시간초과
sys.stdin = open("./input.txt", "r")

R, C = map(int, sys.stdin.readline().split()) # 동굴 크기, R, C

cave = {_:list(''.join(sys.stdin.readline().split())) for _ in range(R)}

N = int(sys.stdin.readline())  # 던진횟수
H = list(map(int, sys.stdin.readline().split())) #던진 높이

dy, dx = [-1,1,0,0],[0,0,1,-1] #[3] 은 바닥

def Mineral():
    cluster = {}
    visit = {}
    queue = deque()
    cnt = 0
    for i in range(R-1):
        for j in range(C):
            if cave[i][j] == 'x': #start
                queue.append((i,j))
                while queue:
                    node = queue.popleft()
                    if node not in visit.keys():
                        for i in range(4):
                            nx, ny = node[0]+dx[i], node[1]+dy[i]
                            if nx < 0 or nx >= R or ny <0 or ny >= C: continue
                            if cave[nx][ny] == 'x':
                                visit[node] = True
                                queue.append((nx,ny))
                                try:
                                    if node not in cluster[cnt]:
                                        cluster[cnt].append(node)
                                except:
                                    cluster[cnt] = []
                                    cluster[cnt].append(node)
                cnt+=1

    if cnt > 0:
        for minerals in cluster.values():
            flag = False
            for loc in minerals:
                if R-1 == loc[0]:
                    flag = True #클러스터에 바닥이 있는지 확인.
                    break
            if not flag: #만약에 떠있으면, 미네랄위치를 아래로 떨어트림.
                level = R
                check_block = []
                for loc in reversed(minerals):
                    if loc[1] in check_block:
                        continue
                    tmp = 1
                    while True:
                        nx, ny = loc[0] + tmp, loc[1]
                        if cave[nx][ny] == 'x' or nx == R-1:
                            break
                        else: tmp += 1
                    check_block.append(loc[1])
                    if level > tmp and tmp != 0:
                        level = tmp
                for loc in reversed(minerals):
                    nx, ny = loc[0] + level, loc[1]
                    cave[loc[0]][loc[1]] = '.'
                    cave[nx][ny] = 'x'

def throw(turn, H):
    if not turn % 2:
        for i in range(C):
            if cave[H][i] == 'x':
                cave[H][i] = '.'
                Mineral()
                break
    else:
        for i in reversed(range(C)):
            if cave[H][i] == 'x':
                cave[H][i] = '.'
                Mineral()
                break

for turn, height in enumerate(H):
    if R-height >= 0 and R-height < R:
        throw(turn, R-height)

#출력
for i in range(R):
    print(' '.join(str(_) for _ in cave[i]))