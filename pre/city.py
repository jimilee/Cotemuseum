import sys
from collections import deque
from itertools import combinations
sys.stdin = open("./input.txt", "r")

H, W, N = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(H)]
for _ in board:
    print(_)

dx, dy = (0,-1,0,1),(-1,0,1,0)

roc = []
for i in range(H):
    for j in range(W):
        roc.append((i,j))

def bfs(targets, start_node, tmp): # 뽑힌 도시 위치들, 처음 스타트 노드, 목표 개수
    result = 0
    cnt = 0
    visit = {}
    queue = deque()
    queue.append(start_node)
    result += board[start_node[0]][start_node[1]]
    while queue:
        node = queue.popleft()
        if node not in visit.keys():
            for i in range(4): # 방향 탐색
                nx, ny = node[0]+dx[i], node[1]+dy[i]
                print(nx, ny , ' search this one. ')
                print(visit.keys())
                if nx < 0 or nx > W or ny <0 or ny > H:
                    continue
                if (nx, ny) in targets and (nx,ny) not in visit.keys(): # 현재 탐색 위치가 뽑힌 위치고,
                    visit[node] = True
                    result += board[nx][ny]
                    queue.append((nx,ny))
                    print(nx, ny, ' is appended.')
                    cnt += 1

    if cnt == tmp-1: return True, result
    else: return False, result

max_result = 0
for data in list(combinations(roc, N)):
    print(data)
    linked, result = bfs(data, data[0], N)
    if linked and max_result < result: # 만약 연결되어있다면 & 값이 더 크면
        max_result = result

print(max_result)
