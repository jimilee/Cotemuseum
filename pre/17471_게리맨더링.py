import sys
from collections import deque

sys.stdin = open("./input.txt", "r")

N = int(sys.stdin.readline()) #갯수 N

population = list(map(int, sys.stdin.readline().split()))
print(population)

graph = {}
check_flag = False
for i in range(N):
    graph[i+1] = list(map(int, sys.stdin.readline().split()))[1:]
    if len(graph[i+1]) > 0:
        check_flag = True

if not check_flag and N!=2: # 두 선거구로 나눌수 없다(연결된 곳 없음).
    print(-1)
    sys.exit()

def get_pop(group):
    pop_group = 0
    for node in group:
        pop_group += population[node-1]
    return pop_group

def is_Linked(group): # 그래프 탐색.
    q = deque()
    q.append(group[0])
    visited = [True]*(len(graph)+1)
    for n in group:
        visited[n] = False
    while q:
        f = q.popleft()
        for t in graph[f]:
            if not visited[t]:
                visited[t] = True
                q.append(t)
    return True if sum(visited) == N + 1 else False

global min_diff
global blue
global red
min_diff = 9999999999
blue = []
red = []

def combinations_2(array, r):
    for i in range(len(array)):
        if r == 1: # 종료 조건
            yield [array[i]]
        else:
            for next in combinations_2(array[i+1:], r-1):
                yield [array[i]] + next

def combination(arr, r):
    arr = sorted(arr)
    used = [0 for _ in range(len(arr))]
    def generate(chosen):
        global min_diff
        global blue
        global red
        if len(chosen) == r:
            red_group = chosen
            blue_group = list(graph.keys() - chosen)
            if len(blue_group) == 1: is_link_blue = True
            else: is_link_blue = is_Linked(blue_group)
            if len(red_group) == 1: is_link_red = True
            else: is_link_red = is_Linked(red_group)
            if is_link_blue and is_link_red:
                diff = abs(get_pop(blue_group) - get_pop(red_group))
                if diff < min_diff:
                    print("\nmin_diff changes : ", min_diff,' to ', diff)
                    min_diff = diff
            return chosen
        start = arr.index(chosen[-1]) + 1 if chosen else 0
        for nxt in range(start, len(arr)):
            if used[nxt] == 0 and (nxt == 0 or arr[nxt - 1] != arr[nxt] or used[nxt - 1]):
                chosen.append(arr[nxt])
                used[nxt] = 1
                generate(chosen)
                chosen.pop()
                used[nxt] = 0
    generate([])

print(graph)
# combinations_2 로 풀기
for i in range(1, len(graph)):
    for chosen in combinations_2(list(graph.keys()), i):
        red_group = chosen
        blue_group = list(graph.keys() - chosen)
        if len(blue_group) == 1:
            is_link_blue = True
        else:
            is_link_blue = is_Linked(blue_group)
        if len(red_group) == 1:
            is_link_red = True
        else:
            is_link_red = is_Linked(red_group)
        if is_link_blue and is_link_red:
            diff = abs(get_pop(blue_group) - get_pop(red_group))
            if diff < min_diff:
                print("\nmin_diff changes : ", min_diff, ' to ', diff)
                min_diff = diff

# combinations_1 재귀 로 풀기
# for i in range(1, len(graph)):
#     combination(graph.keys(), i)
if min_diff != 9999999999:
    print(min_diff)
else:
    print(-1)