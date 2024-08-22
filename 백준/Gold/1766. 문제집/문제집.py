"""
10:27 ~ 10:35
"""


import sys

sys.setrecursionlimit(10**6)
readline = lambda: sys.stdin.readline().strip()

# 1. 전처리
N, M = map(int, readline().split())
GRAPH_SIZE = N + 1
graph = [[] for _ in range(GRAPH_SIZE)]
indegree = [0] * GRAPH_SIZE
for _ in range(M):
    u, v = map(int, readline().split())
    graph[u].append(v)
    indegree[v] += 1

# 2. 순회, 우선순위큐 (min-heap)를 이용해 (난이도) 쉬운 순으로 꺼내도록 한다.

import heapq


visited = [False] * GRAPH_SIZE


def bfs():
    que = []

    for v in range(1, GRAPH_SIZE):
        if indegree[v] == 0:
            heapq.heappush(que, v)

    while que:
        v = heapq.heappop(que)
        if visited[v]:
            continue

        print(v, end=" ")
        visited[v] = True

        for next in graph[v]:
            indegree[next] -= 1
            if indegree[next] == 0:
                heapq.heappush(que, next)


for v in range(1, GRAPH_SIZE):
    if not visited[v]:
        bfs()


