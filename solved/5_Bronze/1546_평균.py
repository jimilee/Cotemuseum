import sys
from collections import deque

sys.stdin = open('../../input.txt', 'r')

N = int(sys.stdin.readline())
score = list(map(int, sys.stdin.readline().split()))

M = max(score)
sum_score = 0
for s in score:
    sum_score += s/M*100
print(sum_score/N)
