import sys
from collections import deque

sys.stdin = open("./input.txt", "r")
T = int(sys.stdin.readline())

result = [0]*2
def fibonacci(n):
    if n == 0:
        result[0] += 1
        return 0
    elif n==1:
        result[1] += 1
        return 1
    else: return fibonacci(n-1) + fibonacci(n-2)

for i in range(T):
    result = [0]*2 #초기화
    n = int(sys.stdin.readline())
    fibonacci(n)
    print(result[0], result[1])