import sys
from collections import deque


sys.stdin = open("./input.txt", "r")
N = int(sys.stdin.readline())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dx, dy = (0,-1,0,1),(-1,0,1,0)

def moving_robot(board):
    visited = [[False]*N for _ in range(N)]
    q = deque()
    q.append([(0,0),(0,1)])
    while q:
        location = q.popleft()
        x,y,x2,y2 = location
        if not visited[x][y]:
            visited[x][y] = True
            for i in range(4):
                nx, ny = x+dx[i], y+dy[i]
                if nx<0 or ny<0 or nx>=N or ny>=N: continue
                if board[nx][ny] == 0:
                    visited[nx][ny] = True
                    board[nx][ny] = board[nx][ny] - 1
                    q.append([(nx,ny),(x,y)])
        if not visited[x2][y2]:
            visited[x2][y2] = True
            for i in range(4):
                nx, ny = x2+dx[i], y2+dy[i]
                if nx<0 or ny<0 or nx>=N or ny>=N: continue
                if board[nx][ny] == 0:
                    visited[nx][ny] = True
                    board[nx][ny] = board[nx][ny] - 1
                    q.append([(nx,ny),(x2,y2)])
        for _ in board:
            print(_)
def solution(board):
    answer = 0
    return answer