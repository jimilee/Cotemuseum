import sys
from collections import deque
sys.stdin = open('../../input.txt', 'r')

N = int(sys.stdin.readline())

data = list(map(int, sys.stdin.readline().split()))

r_nodes = int(sys.stdin.readline())

def count_leaf(tree):
    leaf = 0
    parents = list(tree.keys())
    for p, c in tree.items():
        if p != -1: # 루트 노드는 패스.
            if len(c) == 0: leaf+=1 # 자식(c) 가 없을때 (삭제된 경우)
    return leaf

tree = {}
for i in range(-1,N):
    tree[i] = []
for i,node in enumerate(data): # 트리 생성
    tree[node].append(i)

print(tree)# 삭제 전 트리

q = deque()
q.append(r_nodes)
rm_value = [r_nodes]
while q: #삭제할 노드 탐색
    node = q.popleft()
    if len(tree[node]) > 0: #해당트리에 자식이 있을때
        q.extend(tree[node])
        rm_value +=tree[node]
print('rm_value : ', rm_value)
#노드 삭제
for node in rm_value:
    if node in tree.keys():
        del tree[node]
    for p, c in tree.items():
        for node in c:
            if node in rm_value:
                tree[p].remove(node)
print(tree)

# print(rm_tree)# 삭제 후 트리
print(count_leaf(tree))
