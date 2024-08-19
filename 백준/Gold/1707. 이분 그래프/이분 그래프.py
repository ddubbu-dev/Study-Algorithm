"""
[메모리 초과 이유 분석]
- dfs 연산 최소화; 미방문 노드 연산은 바깥쪽에서
"""

import sys

sys.setrecursionlimit(10**6)  # TODO: 아직 의미 이해를 못함
readline = lambda: sys.stdin.readline().strip()
# readline = input

T = int(readline())

GROUP_INITIAL = 0
GROUP_A = 1
GROUP_B = 2
GROUP_TMP = -1  # index=0 전용


def dfs(graph, start, groups) -> False:  # 이분 그래프인지

    if groups[start] == GROUP_INITIAL:  # 초기화 필요함
        groups[start] = GROUP_A

    # 인접 노드 순회
    for near_v in graph[start]:
        if groups[near_v] == GROUP_INITIAL:
            groups[near_v] = GROUP_B if groups[start] == GROUP_A else GROUP_A
            result = dfs(graph, near_v, groups)

            if not result:
                return False

        elif groups[near_v] == groups[start]:
            return False

    return True


for _ in range(T):
    # 그래프 생성
    V, E = map(int, readline().split())
    GRAPH_SIZE = V + 1
    graph = [[] for _ in range(GRAPH_SIZE)]
    for _ in range(E):
        u, v = map(int, readline().split())
        # 무방향
        graph[u].append(v)
        graph[v].append(u)

    groups = [GROUP_INITIAL] * (GRAPH_SIZE)
    groups[0] = GROUP_TMP

    valid = True
    for v in range(1, GRAPH_SIZE):
        if groups[v] == GROUP_INITIAL:
            groups[v] = GROUP_A
            if not dfs(graph, v, groups):
                valid = False
                break

    print("YES" if valid else "NO")