import copy
import sys
from collections import deque

N, M, K = map(int, sys.stdin.readline().split())


max_key = int(M)
A = {(x,y):[] for y in range(N) for x in range(N)}

directions = [(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1)]
fireballs = {}

def move_fireball(fireballs): # 이동명령
    newfireball = {}
    for i, ball in fireballs.items():
        r,c,m,s,d = ball
        sx, sy = (directions[d][1] * s), (directions[d][0] * s)
        nx, ny = (r + sx + N) % N, (c + sy + N) % N
        A[(r,c)].remove(i)
        A[(nx,ny)].append(i)
        newfireball[i] = [nx,ny,m,s,d]
    fireballs = copy.deepcopy(newfireball)
    return fireballs

def check_overapped(): #
    global max_key
    for loc, balls in A.items():
        if len(balls) >= 2:
            A[loc] = []
            sum_fire(balls, loc)

def sum_fire(balls, loc):
    global max_key
    sumM, sumS = 0, 0
    flag, tmp, evenodd = -1, 0, 0
    evenodd = 0 # 모두 짝수거나 모두 홀수면 0

    for ball in balls:
        r, c, m, s, d = fireballs.pop(ball)
        sumM += m
        sumS += s
        if flag == -1: #모두 짝수거나 홀수인지 판단
            flag = 1
            tmp = d % 2
        elif tmp != d % 2: evenodd = 1

    if int(sumM/5) > 0:
        for i in range(evenodd, 8, 2):
            fireballs[max_key] = [loc[0], loc[1], int(sumM/5), int(sumS/len(balls)), i]
            A[loc].append(max_key)
            max_key += 1


for _ in range(M):
    r, c, m, s, d = map(int, sys.stdin.readline().split())
    fireballs[_] = [r-1, c-1, m, s, d]
    A[(r-1,c-1)].append(_)

for _ in range(K):
    fireballs = move_fireball(fireballs)
    check_overapped()


total = 0
if fireballs:
    for ball in fireballs.values():
        r, c, m, s, d = ball
        total += int(m)
print(total)