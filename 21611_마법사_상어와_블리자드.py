import sys
#마법사 상어의 방향
sx, sy = (-1,1,0,0),(0,0,-1,1)
#격자 탐색 방향
dx, dy = (0,1,0,-1),(-1,0,1,0)
count_ball = {0:0,1:0,2:0,3:0}
def initMap(board):
    Map = {}
    balls = []
    count,n = 1,0
    nloc = (int((N-1)/2),int((N-1)/2))
    while True:
        for d in range(4):
            hol = 1 if d<2 else 0
            for i in range(hol,count+1): #이동 수
                x, y = nloc
                Map[(x,y)]=n
                balls.append(board[x][y])
                if x == 0 and y == 0: return Map, balls
                nx, ny = x+dx[d], y+dy[d]
                if nx < 0 or ny < 0 or nx>=N or ny>=N: continue
                nloc = (nx,ny)
                n+=1
        count += 2

def blizzard(d, s, Shark, Map, balls):
    print(d, s)
    list = []
    x, y = Shark
    for _ in range(s):
        nx, ny = x+sx[d-1], y+sy[d-1]
        list.append((nx,ny))
        x,y = nx, ny
    print(list)
    while list:
        idx = Map[(list.pop())]
        print('remove ', idx)
        if idx < len(balls):
            del balls[idx]
    print(balls)
    return balls

def checkbom(balls):
    box = []
    rm_box = []
    tag = -1
    print('checkbom before... ',balls)
    for i, b in enumerate(balls):
        if i == 0: continue
        if b != tag and b != 0:
            if len(box) >= 4:
                rm_box.extend(box)
            box.clear()
            tag = b
            box.append(i)
        elif b == tag:
            box.append(i)
        elif b == 0:
            rm_box.append(i)
    if len(box) >= 4 and tag != 0:
        rm_box.extend(box)
    if len(rm_box)== 0: return False, balls
    while rm_box: #제거
        index = rm_box.pop()
        count_ball[balls[index]] += 1 # 폭발한 구슬 카운트
        del balls[index]
    print('checkbom after... ',balls)
    return True, balls

def change_balls(balls, max_len):
    print('================ change_balls ===================')
    print(balls)
    ball_cnt = 0
    new_balls = [0]
    tag = -1
    for i, b in enumerate(balls):
        if i == 0 : continue
        if b != tag:
            if tag != -1:
                new_balls.append(ball_cnt) # A
                new_balls.append(tag) # B
            ball_cnt = 0
            tag = b
            ball_cnt += 1
        elif b == tag:
            ball_cnt += 1
    new_balls.append(ball_cnt) # A
    new_balls.append(tag) # B
    print(new_balls[:max_len])
    return new_balls[:max_len]


sys.stdin = open('./input.txt', 'r')
N, M = map(int, sys.stdin.readline().split())
Shark = (int((N-1)/2),int((N-1)/2))
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

Map, balls = initMap(board)
print(Map)
print(balls)
for i in range(M):
    d, s = map(int, sys.stdin.readline().split())
    print(i , '번째 블리자드 후.',balls)
    balls = blizzard(d, s, Shark, Map, balls)
    while True:
        rm_ball, balls = checkbom(balls)
        if not rm_ball:
            break
    balls = change_balls(balls, N*N)
    print(rm_ball, balls)
print(count_ball)
print(1*count_ball[1]+2*count_ball[2]+3*count_ball[3])
