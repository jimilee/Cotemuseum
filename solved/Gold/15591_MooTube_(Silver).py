import sys
from collections import deque

sys.stdin = open("./input.txt", "r")

N, Q = map(int, sys.stdin.readline().split()) # N, Q

USADO = dict()

for _ in range(N-1):
    p, q, r = map(int,sys.stdin.readline().split())
    if p in USADO.keys():
        USADO[p].append([q,r])
    else:
        USADO[p]=[[q,r]]
    if q in USADO.keys():
        USADO[q].append([p,r])
    else:
        USADO[q]=[[p,r]]

def get_recommands(k, v):
    visited = [False] * (N + 1) #dict보다 빠름.
    need_visit = deque()
    need_visit.append([v, 1000000000])
    while need_visit:
        node, val = need_visit.popleft()
        if not visited[node] and val >= k:
            visited[node] = True
            need_visit.extend(USADO[node])
    return visited.count(True) - 1

for i in range(Q):
    k, v = map(int, sys.stdin.readline().split())
    print(get_recommands(k, v))
