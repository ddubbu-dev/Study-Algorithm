from collections import deque

import sys
readline = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**6)
# readline = input


N = int(readline())
M = int(readline())

# 그래프 초기화
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, readline().split())

    graph[u].append(v)
    graph[v].append(u)


visited = [False] * (N + 1)


def dfs(start_v):
    visited[start_v] = True

    for child_v in graph[start_v]:
        if not visited[child_v]:
            dfs(child_v)


dfs(1)

visits = len(list(filter(lambda x: x, visited)))
print(visits - 1)  # 1 제외
