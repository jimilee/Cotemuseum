import sys
# 벨만 포드 알고리즘.
INF = 9999999999
sys.stdin = open("../../../input.txt", "r")

N, M = map(int, sys.stdin.readline().split()) # 도시 N, 버스 M

data = []
dist = [INF] * (N+1)
for b in range(M): # 버스 스케줄 수
    s, d, c =  map(int, sys.stdin.readline().split())
    data.append([s, d, c])

def bf(start_node): # 벨만 포드 알고리즘
    dist[start_node] = 0 # 시작 노드는 0
    for i in range(N):
        for j in range(M):
            node = data[j][0]
            next_node = data[j][1]
            cost = data[j][2]
            # 다른 도시를 경유해서 이동하는 경로가 더 짧다면.
            if dist[node] != INF and dist[next_node] > dist[node] + cost:
                dist[next_node] = dist[node] + cost
                if i == N-1: # n -1번 반복했는데도 갱신되면 무한음수
                    return True
if bf(1):
    print('-1')
else:
    for i in range(2, N+1):
        if dist[i] == INF: print(-1)
        else: print(dist[i])