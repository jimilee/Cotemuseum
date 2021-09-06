import sys
from collections import deque

sys.stdin = open('../../input.txt', 'r')
N, M = map(int, sys.stdin.readline().split())
non_listen = [sys.stdin.readline().split('\n')[0] for _ in range(N+M)]
non_listen.sort()
non_li_seen = deque()
tmp = ''
for i in range(len(non_listen)):
    if tmp == non_listen[i]:
        non_li_seen.append(non_listen[i])
        i += 2
    else: tmp = non_listen[i]
print(len(non_li_seen))
while non_li_seen:
    print(non_li_seen.popleft())