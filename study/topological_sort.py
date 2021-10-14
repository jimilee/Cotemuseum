from collections import deque

# 노드의 개수 v와 DAG
v= 7
adj_list = [[1, 2], [1, 5], [2, 3], [2, 6], [3, 4], [4, 7], [5, 6], [6, 4]]

# 위상 정렬
def topology_sort(v, adj_list):
    answer = [] # 알고리즘 수행 결과를 담을 리스트
    q = deque() # deque 사용

    # 모든 노드에 대한 진입차수
    indegree = [0] * (v + 1)
    # 각 노드에 연결된 간선 정보를 담기 위한 그래프 초기화
    graph = [[] for i in range(v + 1)]

    # 방향 그래프의 모든 간선 정보 갱신하기
    for a, b in adj_list:
        graph[a].append(b) # 정점 A에서 B로 이동 가능
        # 진입 차수를 1 증가
        indegree[b] += 1

    # 처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)

    # 큐가 빌 때까지 반복
    while q:
        # 큐에서 원소 꺼내기
        this = q.popleft()
        answer.append(str(this))
        # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
        for i in graph[this]:
            indegree[i] -= 1
            # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[i] == 0:
                q.append(i)
    # 결과 출력
    print(' '.join(answer))

topology_sort(v, adj_list)