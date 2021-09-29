import sys
from itertools import permutations
import operator
sys.stdin = open('./input.txt', 'r')

cal = {0:'+', 1:'-', 2:'*', 3:'/'}
N = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
limit = list(map(int, sys.stdin.readline().split()))
cals = []
for i, v in enumerate(limit):
    for _ in range(v):
        cals.append(cal[i])
print(N)
print(cals)
def calculator(A,B,O):
    if O == '+':
        return A+B
    if O == '-':
        return A-B
    if O == '*':
        return A*B
    if O == '/':
        return int(A/B)
def make_cal():
    min = 1000000000
    max = -1000000000
    for cal in permutations(range(N-1), N-1):
        print(cal)
        for i, c in enumerate(cal):
            print(data[i], data[i+1],cals[c])
            if i == 0:
                res = calculator(data[i], cals[c], data[i+1])
                print('res : ', res)
            else:
                res = calculator(res, data[i+1], cals[c])
                print('res : ', res)
        if res < min:
            min = res
        if res > max:
            max = res
    print(max)
    print(min)
make_cal()