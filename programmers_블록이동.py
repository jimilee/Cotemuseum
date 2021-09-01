import sys
from collections import deque


sys.stdin = open("./input.txt", "r")
N = int(sys.stdin.readline())
board = [list(map(int, sys.stdin.readline().split(','))) for _ in range(N)]
dx, dy = (0,-1,0,1),(-1,0,1,0)

def moving_robot(board):
    N = len(board)
    visited = []
    q = deque()
    q.append([0,0,0,1,0]) # x,y,x2,y2,d # d = 0이면 가로, 1이면 세로
    while q:
        location = q.pop()
        print('\nlocation ',location)

        x,y,x2,y2,state = location
        pos = {(x,y), (x2,y2)}
        print('visited_,', state)
        print('==== borad ====')
        for _ in board:
            print(_)
        if pos not in visited:
            visited.append(pos)
            #xy
            statxy = state # x, y
            for i in range(4):
                nx, ny = x+dx[i], y+dy[i]
                if nx<0 or ny<0 or nx>=N or ny>=N or (nx==x2 and ny==y2) or board[nx][ny]==1: continue
                if abs(nx - x) == statxy and {(x,y), (nx,ny)} not in visited: #방향이 로봇과 같은 방향으로 이동할때.
                    board[nx][ny] = board[x][y] - 1
                    print('push. xy/ 방향같게 이동.',nx,ny,x,y,statxy)
                    for _ in board:
                        print(_)
                    q.append([nx,ny,x,y,statxy])

                else: #회전 or 이동
                    cx, cy = 0,0 #check location
                    if statxy == 1: #수직일때
                        cx, cy = x2, ny
                    else: #수평일때
                        cx, cy = nx, y2
                    if board[cx][cy] != 1: #이동 or 회전 가능 확인.
                        #이동
                        if {(cx,cy), (nx,ny)} not in visited:
                            board[cx][cy] = board[x][y] - 1
                            print('push. xy/ 다른방향 이동',nx,ny,cx,cy,statxy)
                            for _ in board:
                                print(_)
                            q.append([nx,ny,cx,cy,statxy])
                        #회전
                        if {(x,y), (nx,ny)} not in visited:
                            statxy = abs(statxy-1) #상태 회전. 0->1, 1->1
                            board[nx][ny] = board[x][y] - 1
                            print('push. xy/ 다른방향 회전',nx,ny,x,y,statxy)
                            for _ in board:
                                print(_)
                            q.append([nx,ny,x,y,statxy])
            #xy2
            statxy2 = state
            for i in range(4):
                nx, ny = x2+dx[i], y2+dy[i]
                print(nx, ny,statxy2, '보드 이동')
                if nx<0 or ny<0 or nx>=N or ny>=N or (nx==x and ny==y) or board[nx][ny] == 1: continue
                if abs(nx - x2) == statxy2 and {(x2,y2), (nx,ny)} not in visited: #로봇의 방향과 같은방향 이동
                    board[nx][ny] = board[x2][y2] - 1
                    print('push. x2y2/ 같은방향 이동 ',nx,ny,x2,y2,statxy2)
                    for _ in board:
                        print(_)
                    q.append([nx,ny,x2,y2,statxy2])
                else: #회전
                    cx, cy = 0,0 #check location
                    if statxy2 == 1: cx, cy = x, ny #수직일때
                    else: cx, cy = nx, y

                    if board[cx][cy] != 1: #이동 or 회전 가능 확인.
                        #이동
                        if {(cx,cy), (nx,ny)} not in visited:
                            board[cx][cy] = board[x2][y2] - 1
                            print('push. x2y2/ 다른방향 이동 ',nx,ny,cx,cy,statxy2)
                            for _ in board:
                                print(_)
                            q.append([nx,ny,cx,cy,statxy2])
                        #회전
                        if {(x2,y2), (nx,ny)} not in visited:
                            statxy2 = abs(statxy2-1) #상태 회전. 0->1, 1->1
                            board[nx][ny] = board[x2][y2] - 1
                            print('push. x2y2/ 다른방향 회전 ',nx,ny,x2,y2,statxy2)
                            for _ in board:
                                print(_)
                            q.append([nx,ny,x2,y2,statxy2])
        print(q)


    return int(abs(board[N-1][N-1]))


def solution(board):
    answer = moving_robot(board)
    print(answer)
    return answer
