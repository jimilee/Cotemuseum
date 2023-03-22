import sys
from collections import deque

sys.stdin = open("./input.txt", "r")
N = int(sys.stdin.readline())

HanSu = [True]*(N+1)
def isHanSu(n):
    numbers = deque(reversed(list(str(n))))
    data = 999
    num_box = int(numbers.popleft())
    while numbers:
        num = int(numbers.popleft())
        if data == 999: #첫번째
            data = num_box - num
        elif data != num_box - num:
            HanSu[n] = False
            break
        num_box = num

for i in range(1,N+1):
    isHanSu(i)

print(HanSu.count(True)-1) #0은 빼줌