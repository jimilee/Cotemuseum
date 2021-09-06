import sys
from collections import deque

sys.stdin = open('../../input.txt', 'r')

T = int(sys.stdin.readline())
def isVPS(arr):
    left = []
    right = []
    for ps in arr:
        if ps =='(':
            try: right.pop()
            except: left.append(ps)
        elif ps ==')':
            try: left.pop()
            except: return 'NO'
    print(left)
    print(right)
    if len(left) == len(right):return 'YES'
    return 'NO'

for _ in range(T):
    print('T :', _)
    print(isVPS(list(sys.stdin.readline())))
