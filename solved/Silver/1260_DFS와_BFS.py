import sys
from collections import deque
sys.stdin = open("../../input.txt", "r")

N, M, V = map(int, sys.stdin.readline().split()) #정점의 갯수 N, 간선 수 M, 탐색을 시작할 정점의 번호 V

graph = {}
list = []
for i in range(M):
    node1, node2 = map(int, input().split())
    if i+1 not in graph.keys():
        graph[i+1] = []
    # 양방향 그래프 저장
    try:
        graph[node1].append(node2)
    except:
        graph[node1] = []
        graph[node1].append(node2)
    try:
        graph[node2].append(node1)
    except:
        graph[node2] = []
        graph[node2].append(node1)

for key, list in graph.items():
    list.sort()

def bfs(graph, start_node):
    visit = {}
    queue = deque()
    queue.append(start_node)
    while queue:
        node = queue.popleft()
        if node not in visit.keys():
            visit[node] = True
            queue.extend(graph[node])
    return [str(key) for key in visit.keys()]

def dfs(graph, start_node):
    visit = {}
    stack = []
    stack.append(start_node)

    while stack:
        node = stack.pop()
        if node not in visit.keys():
            visit[node] = True
            stack.extend(reversed(graph[node]))

    return [str(key) for key in visit.keys()]

print(' '.join(dfs(graph, V)))
print(' '.join(bfs(graph, V)))