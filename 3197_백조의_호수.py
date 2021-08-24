import sys
from collections import deque
sys.stdin = open("./input.txt","r")

x, y = map(int, sys.stdin.readline().split()) #호수 넓이 x,y
hosu = [list(input().strip()) for _ in range(x)] #2차원 리스트 형식으로 문자열 저장
visit = [[0 for _ in range(y)] for _ in range(x)]

wc = [[False]*y for _ in range(x)]
sc = [[False]*y for _ in range(x)]

wq1, wq2 = deque(), deque()
sq1, sq2 = deque(), deque()
whereL = []

ex, ey, ans = 0,0,0
dx, dy = (0,-1,0,1),(-1,0,1,0)
def water():
    while wq1:
        x,y = wq1.popleft()
        hosu[x][y] = '.'
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if nx < 0 or nx >= x or ny <0 or ny >=y or wc[nx][ny]:
                continue
            if hosu[nx][ny] == '.':
                wq1.append((nx,ny))
            else:
                wq2.append((nx,ny))
            wc[nx][ny] = True

def swan():
    while sq1:
        x,y = wq1.popleft()
        if x == ex and y == ey:
            return True
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if nx < 0 or nx >= x or ny <0 or ny >=y or wc[nx][ny]:
                continue
            if hosu[nx][ny] == '.':
                sq1.append((nx,ny))
            else:
                sq2.append((nx,ny))
            sc[nx][ny] = True
    return False

for i in range(x):
    for j in range(y):
        if hosu[i][j] == 'L':
            if not sq1:
                sq1.append((i,j))
                sc[i][j] = True
            else:
                ex, ey = i,j
            hosu[i][j] = '.'
        if hosu[i][j] == '.':
            wq1.append((i,j))
            wc[i][j] = True


def winter_hosu():
    global hosu
    day = 0
    found_one, found_two, meet = False, False, False
    while not meet:
        for i in range(0, x):
            for j in range(0, y):
                if hosu[i][j] == 'X':
                    if hosu[i+1][j] == '.' and i<x-1:
                        next_day[i][j] = '.'
                        break
                    if hosu[i-1][j] == '.' and i>0:
                        next_day[i][j] = '.'
                        break
                    if hosu[i][j+1] == '.' and j<y-1:
                        next_day[i][j] = '.'
                        break
                    if hosu[i][j-1] == '.' and j >0:
                        next_day[i][j] = '.'
                        break
                elif hosu[i][j] == 'L' and not found_two:
                    whereL.append((i,j))
                    if found_one: found_two = True
        hosu = next_day
        day += 1
        if meet():
            meet = True
            print(day)

winter_hosu()