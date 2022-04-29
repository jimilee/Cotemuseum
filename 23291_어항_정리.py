import copy
import sys
from collections import deque

sys.stdin = open("./input.txt", "r")

N, K = map(int, sys.stdin.readline().split()) # 어항수 N, 물고기 수 차이 K
H =int(N/2)
fish_in_ball = list(map(int, sys.stdin.readline().split()))
roll_list = deque()
fish_ball = [[0]*N for _ in range(H)]
fish_ball.append(list(fish_in_ball))

'''
TODO : 공중부양 작업 완료 후 작업들....
'''
for _ in fish_ball:
    print(_)

block = [[3,5],[3,14]]
def make_rotate_loc(start, block, fish_ball): # start 는 시작 좌표.
    tmp = copy.deepcopy(fish_ball)
    sx, sy = start
    w = len(block)
    h = len(block[0])
    sx, sy = sx-h, sy+h
    print(sx, sy, w, h)
    # for _ in block:
    #     print(_)
    new_block = [[0]*w for _ in range(h)]
    cnt = 0
    for j in range(h):
        for i in range(w):
            new_block[cnt][(w-1)-i] = block[i][j]
        cnt+=1
    print('=== new block ===')
    for _ in new_block:
        print(_)

    for i in range(len(new_block)): # h
        for j in range(len(new_block[0])): # w
            print(new_block[i][j], ' (',i,j,')','-> (',sx+i, sy+j,')', tmp[i][j])
            tmp[sx+i][sy+j] = new_block[i][j]
            tmp[i][j] = 0
    print('=== delete moved block ===')
    for i in range(H+1):
        del tmp[i][:sy]
        tmp[i].extend([0]*sy)

    return tmp
# make_rotate_loc((4,2),block, fish_ball)

def roll_fish_ball(fish_ball):
    block = [[0]*N for _ in range(H+1)]
    sx, sy = -1,999 # x는 가장 큰수, y는 가장 작은수
    while roll_list:
        x, y, f = roll_list.popleft()
        if sx < x: sx = x
        if sy > y: sy = y
        print(x, y, 'fish in.', sx, sy)
        block[x][y] = f
    nblock = []
    for _ in block:
        print(_)
    print('...')
    for i in range(H + 1): # 0 제거
        while 0 in block[i]:
            block[i].remove(0)
        if len(block[i]) > 0:
            nblock.append(block[i])
    print(len(nblock[0]))
    print(sx, sy)
    fish_ball = make_rotate_loc((sx,sy), nblock,fish_ball)
    return fish_ball


print('수가 가장 적은 물고기에 1마리 넣기.')
min_f = min(fish_in_ball)
for i in range(H+1):
    for j in range(N):
        if fish_ball[i][j] == min_f:
            fish_ball[i][j]+=1

for t in range(5):
    print('=========', t, '=========')
    r_flag = False
    for i in range(H+1):
        for j in range(N):
            try:
                if fish_ball[i][j] != 0 and fish_ball[i+1][j] != 0:
                    roll_list.append((i,j, fish_ball[i][j]))
                    roll_list.append((i+1,j, fish_ball[i+1][j]))
                elif fish_ball[i][j] != 0 and fish_ball[i+1][j] == 0:
                    print('rolling done.')
                    roll_list.clear()
                    r_flag = True
                    break
            except: continue
        if r_flag: break

    if not r_flag:
        if len(roll_list) == 0:
            roll_list.append((H,0, fish_ball[H][0]))

        print(roll_list)
        fish_ball = roll_fish_ball(fish_ball)

        for _ in fish_ball:
            print(_)

    else:
        print('공중 부양 작업 완료.')
