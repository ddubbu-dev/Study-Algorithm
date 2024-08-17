from collections import deque

import sys
readline = lambda: sys.stdin.readline().rstrip()
# readline = input

N, M, start_v = map(int, readline().split())

G = {}
for _ in range(M):  # 양방향 간선!
    v1, v2 = map(int, readline().split())

    if G.get(v1):
        prev = G[v1]
        # 작은 것부터 먼저 방문하기 위해 마지막에 넣어줘야함
        new_child = sorted(prev + [v2], reverse=True)
        G[v1] = new_child
    else:
        G[v1] = [v2]

    if G.get(v2):
        prev = G[v2]
        # 작은 것부터 먼저 방문하기 위해 마지막에 넣어줘야함
        new_child = sorted(prev + [v1], reverse=True)
        G[v2] = new_child
    else:
        G[v2] = [v1]

def dfs():
    stack = deque([start_v])
    visited = [False] * (N + 1)

    while stack:
        v = stack.pop()

        if visited[v]:
            continue

        print(v, end=" ")
        visited[v] = True

        try:
            for child_v in G[v]:  # Q. dict key 값 없을 때 에러 어떻게 나는지 궁금함
                if not visited[child_v]:
                    stack.append(child_v)
        except:
            continue


def bfs():
    que = deque([start_v])
    visited = [False] * (N + 1)

    while que:
        v = que.popleft()

        if visited[v]:
            continue

        print(v, end=" ")
        visited[v] = True

        try:
            child = sorted(G[v])  # dfs와 달리 오름차순으로, 선입선출
            for child_v in child:  # Q. dict key 값 없을 때 에러 어떻게 나는지 궁금함
                if not visited[child_v]:
                    que.append(child_v)
        except:
            continue


dfs()
print()
bfs()
