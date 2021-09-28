import sys
from collections import deque
sys.stdin = open('../../input.txt', 'r')

def bfs():
    q.append([0, 0, 0])
    dist[0][0][0] = 1
    while q:
        x, y, z = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx >= N or ny >= M or nx < 0 or ny < 0: continue
            if board[nx][ny] == 0 and dist[nx][ny][z] == -1: # 길이고, 방문하지 않았을때
                dist[nx][ny][z] = dist[x][y][z] + 1
                q.append([nx, ny, z])
            elif z == 0 and board[nx][ny] == 1 and dist[nx][ny][z + 1] == -1: # 벽일때, 벽을 부수지 않았을때 z = 0
                dist[nx][ny][z + 1] = dist[x][y][z] + 1
                q.append([nx, ny, z+1]) # 해당 벽을 부순 상태 append
        print('\n================================')
        for p in dist:
            print(p)
        print('================================\n')

N, M = map(int,sys.stdin.readline().split())
dx, dy = (0,0,1,-1),(1,-1,0,0)
board = [list(map(int, input())) for _ in range(N)]
dist = [[[-1] * 2 for _ in range(M)] for _ in range(N)]
q = deque()
bfs()
res1, res2 = dist[N - 1][M - 1][0], dist[N - 1][M - 1][1] # 벽을 부수지 않았을때, 벽을 부수었을때
if res1 == -1 and res2 != -1:
    print(res2)
elif res1 != -1 and res2 == -1:
    print(res1)
else:
    print(min(res1, res2))

# def bfs(board): #시간초과.
#     visited = [[False]*M for _ in range(N)]
#     dist = [[-1]*M for _ in range(N)]
#     q = deque()
#     q.append((0,0)) #시작노드
#     dist[0][0] = 1
#     print('\n========= start board ===========')
#     for p in board:
#         print(p)
#     print('================================\n')
#     while q:
#         x, y = q.popleft()
#         visited[x][y] = True
#         for d in range(4):
#             nx, ny = x+dx[d], y+dy[d]
#             if nx >= N or ny >= M or nx < 0 or ny < 0 or board[nx][ny] == '1': continue
#             if not visited[nx][ny]:
#                 q.append((nx,ny))
#                 dist[nx][ny] = dist[x][y]+1
#         print('\n================================')
#         for p in dist:
#             print(p)
#         print('================================\n')
#     return dist[N-1][M-1]
#
# def get_minimum():
#     min_result = 99999
#     board = [list(map(str, sys.stdin.readline().strip())) for _ in range(N)]
#     print(board)
#     for i in range(N):
#         for j in range(M):
#             if board[i][j] == '1': # 벽일때
#                 board[i][j] = '0' # 벽 부수기
#                 res = bfs(board)
#                 print('[{0}, {1}] : result : {2}.'.format(i,j,res))
#                 if res == -1:
#                     board[i][j] = '1' # 다시 원상복구
#                     continue
#                 elif min_result > res:
#                     min_result = res
#                     board[i][j] = '1' # 다시 원상복구
#     if min_result == 99999:
#         print(-1)
#     else: print(min_result)
# get_minimum()