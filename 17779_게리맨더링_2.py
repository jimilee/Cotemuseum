import copy
import sys
from collections import deque

sys.stdin = open("./input.txt", "r")
N = int(sys.stdin.readline())

population = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
regions = [[0]*N for _ in range(N)]

for _ in population:
    print(_)

def permutation(array, r):
    for i in range(len(array)):
        if r == 1: #종료
            yield [array[i]]
        else:
            for next in permutation(array[:i]+array[i:],r-1):
                yield [array[i]] + next

def combination(array, r):
    for i in range(len(array)):
        if r == 1: #종료
            yield [array[i]]
        else:
            for next in combination(array[i:], r-1):
                yield [array[i]]+next

def make_one_region(regions,x,y):
    for i in range(x):
        for j in range(y+1):
            if regions[i][j] != 1:
                group_pop[1] += population[i][j]
                regions[i][j] = 1
def make_two_region(regions,x,y):
    for i in range(x+1):
        for j in range(y+1,N):
            if regions[i][j] != 2:
                group_pop[2] += population[i][j]
                regions[i][j] = 2
def make_three_region(regions,x,y):
    for i in range(x, N):
        for j in range(y):
            if regions[i][j] != 3:
                regions[i][j] = 3
                group_pop[3] += population[i][j]

def make_four_region(regions,x,y):
    for i in range(x+1, N):
        for j in range(y,N):
            if regions[i][j] != 4:
                regions[i][j] = 4
                group_pop[4] += population[i][j]
def make_five_region(regions):
    for i in range(N):
        try:
            start = regions[i].index(5)
            if regions[i].count(5) > 1:
                for _ in range(start+1,N):
                    if regions[i][_] == 0:
                        regions[i][_] = 5
                        group_pop[5] += population[i][_]
        except:
            continue

def make_grid(regions, x, y, d1, d2):
    regions[x][y] = 5
    group_pop[5] += population[x][y]
    make_one_region(regions,x,y)

    for tl in range(d1):
        nx, ny = x + 1, y - 1
        if nx < 0 or ny < 0 or nx >= N or ny >= N:
            return False
        if regions[nx][ny] != 5:
            regions[nx][ny] = 5
            group_pop[5] += population[nx][ny]

        make_one_region(regions, nx, ny)
        x, y = nx, ny
    make_three_region(regions, x, y)
    for bl in range(d2):
        nx, ny = x + 1, y + 1
        if nx < 0 or ny < 0 or nx >= N or ny >= N:
            return False
        if regions[nx][ny] != 5:
            regions[nx][ny] = 5
            group_pop[5] += population[nx][ny]

        make_three_region(regions, nx, ny)
        x, y = nx, ny
    make_four_region(regions, x, y)
    for br in range(d1):
        nx, ny = x - 1, y + 1
        if nx < 0 or ny < 0 or nx >= N or ny >= N:
            return False
        if regions[nx][ny] != 5:
            regions[nx][ny] = 5
            group_pop[5] += population[nx][ny]

        make_four_region(regions, nx, ny)
        x, y = nx, ny
    make_two_region(regions, x, y)
    for tr in range(d2):
        nx, ny = x - 1, y - 1
        if nx < 0 or ny < 0 or nx >= N or ny >= N:
            return False
        if regions[nx][ny] != 5:
            regions[nx][ny] = 5
            group_pop[5] += population[nx][ny]

        make_two_region(regions, nx, ny)
        x, y = nx, ny
    make_five_region(regions)
    return True
#
min_value = 99999999
for data in permutation(list(range(1,N)), 4):
    regions = [[0] * N for _ in range(N)]
    group_pop = {_ + 1: 0 for _ in range(5)}
    x,y,d1,d2 = data
    if make_grid(regions, x,y,d1,d2):
        print('result')
        print(group_pop)
        diff = max(group_pop.values()) - min(group_pop.values())
        if min_value > diff:
            min_value = diff
        for _ in regions:
            print(_)
print(min_value)