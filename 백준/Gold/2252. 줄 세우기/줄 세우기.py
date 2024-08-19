from collections import deque
import sys

sys.setrecursionlimit(10**6)  # TODO: 아직 의미 이해를 못함
readline = lambda: sys.stdin.readline().strip()
# readline = input


N, M = map(int, readline().split())
GRAPH_SIZE = N + 1

graph = [[] for _ in range(GRAPH_SIZE)]
indegree = [0 for _ in range(GRAPH_SIZE)]  # idx=0 조심

for _ in range(M):
    u, v = map(int, readline().split())
    graph[u].append(v)
    indegree[v] += 1

que = deque()

# 출발점 리스트업
for v in range(1, GRAPH_SIZE):
    if indegree[v] == 0:
        que.append(v)

while que:
    v = que.popleft()
    print(v, end=" ")
    indegree[v] -= 1

    for near in graph[v]:
        indegree[near] -= 1

        if indegree[near] == 0:
            que.append(near)