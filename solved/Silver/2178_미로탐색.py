import sys
from collections import deque

sys.stdin = open("../../input.txt", "r")

N, M = map(int, sys.stdin.readline().split()) #갯수 N, 간선 수 M
dx, dy = (0,-1,0,1),(-1,0,1,0)
maze = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]
visit = [[0 for _ in range(M)] for _ in range(N)]

def bfs(maze, start_node):
    visit = {}
    queue = deque()
    queue.append(start_node)
    while queue:
        node = queue.popleft()
        if node not in visit.keys():
            for i in range(4):
                nx, ny = node[0]+dx[i], node[1]+dy[i]
                if nx < 0 or nx >= N or ny <0 or ny >= M:
                    continue
                if maze[nx][ny] == 1:
                    visit[node] = True
                    maze[nx][ny] = maze[node[0]][node[1]]+1

                    queue.append((nx,ny))
    return maze[N-1][M-1]

print(bfs(maze, (0,0)))