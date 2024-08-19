"""
[예제]
n = 5  # 정점 수
m = 4  # 간선 수

1 -> 2 -> 4, 5
1 -> 3
"""

from collections import deque

graph = [[], [2], [4, 5], [], [], []]
GRAPH_SIZE = len(graph)
indegree = [0] * (GRAPH_SIZE)  # 진입차수

for edges in graph:  # 진입 차수 테이블
    for end_v in edges:
        indegree[end_v] += 1


def topology_sort():
    result = []
    que = deque()

    for v in range(1, GRAPH_SIZE):
        if indegree[v] == 0:
            que.append(v)

    while que:
        print(indegree)

        start = que.popleft()
        result.append(start)
        for near in graph[start]:
            indegree[near] -= 1  # 진입차수 줄이기
            if indegree[near] == 0:
                que.append(near)

    for v in result:
        print(v, end=" ")


topology_sort()  # 출력 : 1 2 3 4 5
