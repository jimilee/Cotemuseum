import sys
sys.stdin = open("input.txt","r")


x, y = map(int, sys.stdin.readline().split()) #호수 넓이 x,y
hosu = [list(map(str, sys.stdin.readline()[:y])) for _ in range((x))] #2차원 리스트 형식으로 문자열 저장
visit = [[0 for _ in range(y)] for _ in range(x)]
next_day = hosu
print(hosu)
print(next_day)

whereL = []


def meet(): #길찾기 알고리즘.
    queue = []
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

    queue.append(whereL[0])
    visit[whereL[0][0]][whereL[0][1]] = 1

    while queue:
        x,y = queue.pop(0)
        if x == whereL[1][0] and y == whereL[1][1]:
            return True

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx<x and 0<= ny < y:
                if visit[nx][ny] == 0 and hosu[nx][ny] == '.':
                    visit[nx][ny] = visit[x][y] + 1
                    queue.append((nx,ny))


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