
import sys
readline = lambda: sys.stdin.readline().strip()

N, M, V = map(int, readline().split())
GRAPH_SIZE = N + 1
graph = [[] for _ in range(GRAPH_SIZE)]
for _ in range(M):
    u, v = map(int, readline().split())
    graph[u].append(v)
    graph[v].append(u)

for idx in range(len(graph)): # 작은 정점부터 순회
    graph[idx] = sorted(graph[idx])


# ================ DFS ================
visited = [False] * GRAPH_SIZE


def dfs(v):
    visited[v] = True
    print(v, end=" ")

    for near in graph[v]:
        if not visited[near]:
            dfs(near)


dfs(V)
print()

# ================ BFS ================
from collections import deque


def bfs(v):
    visited = [False] * GRAPH_SIZE
    que = deque([v])

    while que:
        v = que.popleft()

        visited[v] = True
        print(v, end=" ")

        for near in graph[v]:
            if not visited[near]:
                que.append(near)
                visited[near] = True


bfs(V)
