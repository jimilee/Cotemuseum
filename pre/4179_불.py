import sys
from collections import deque

sys.stdin = open("./input.txt", "r")

N, M = map(int, sys.stdin.readline().split()) #갯수 N, 간선 수 M
dx, dy = (0,-1,0,1),(-1,0,1,0)
maze = [list(map(str, sys.stdin.readline().strip())) for _ in range(N)]
visit_m = [[-1 for _ in range(M)] for _ in range(N)]
fire_loc = deque()
def bfs(maze, start_node):
    visit = {}
    queue = deque()
    queue.append(start_node)
    while queue:
        cur_fire_loc = deque()
        node = queue.popleft()
        if fire_loc:
            while fire_loc:
                node = fire_loc.popleft()
                for i in range(4):
                    nx, ny = node[0] + dx[i], node[1] + dy[i]
                    if nx < 0 or nx >= N or ny < 0 or ny >= M:
                        continue
                    if maze[nx][ny] == '.' or maze[nx][ny] == 'J':
                        maze[nx][ny] = 'F'
                        cur_fire_loc.append((nx,ny))

        for i in range(4):
            nx, ny = node[0]+dx[i], node[1]+dy[i]
            print('nx, ny : ', nx, ny)
            if nx < 0 or nx >= N or ny <0 or ny >= M:
                continue

            if maze[nx][ny] == '.' and visit_m[nx][ny] == -1:
                if nx == N-1 or ny == M-1 or nx == 0 or ny == 0:
                    print('nx, ny : ', nx, ny)
                    return visit_m[node[0]][node[1]]+1
                visit[node] = True
                visit_m[nx][ny] = visit_m[node[0]][node[1]]+1
                queue.append((nx,ny))


        print('+++ maze +++++++++++++++++++++++++++')
        for _ in maze:
            print(_)
        print('++++++++++++++++++++++++++++++++++')
        print('--- visit_m --------------------------')
        for _ in visit_m:
            print(_)
        print('----------------------------------')
    return 'IMPOSSIBLE'

jihoon = None
for i in range(N):
    for j in range(M):
        if maze[i][j] == 'J':
            jihoon = (i,j)
            visit_m[i][j] = 1
            if i == N - 1 or j == M - 1 or i == 0 or j == 0:
                print(1)
                exit(0)
        if maze[i][j] == 'F':
            fire_loc.append((i,j))
print(bfs(maze, jihoon))
