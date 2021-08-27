import sys
from collections import deque

sys.stdin = open("../../input.txt", "r")

N = int(sys.stdin.readline())
A = {}

def getNum():
    Num = ''
    for i in range(len(str(N))):
        c = sys.stdin.read(1)
        if c.isdigit():
            Num = Num + c
        else: return int(Num)

for _ in range(N):
    num = getNum()
    if num in A.keys():
        print(num)
        break
    else: A[num]= True