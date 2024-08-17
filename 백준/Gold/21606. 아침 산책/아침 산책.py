"""
[문제 이해]
- N개의 노드, N-1 엣지
- 시작점, 끝점 모두 실내 / 그 외 모두 실외
- 탐색 가짓수

[주의]
- 인덱스 1 ~ N 보장하기

[질문]
- 시작점, 끝점이 같을 수도 있나?
"""

import sys
readline = lambda : sys.stdin.readline().strip()
sys.setrecursionlimit(10**9)

EMPTY_0 = -1

N = int(readline())
NUMS = N + 1
is_internal_arr = [EMPTY_0] + [int(c) for c in readline()]


# 그래프 만들기
graph = [[] for _ in range(NUMS)]
for _ in range(N - 1):
    u, v = map(int, readline().split())

    graph[u].append(v)
    graph[v].append(u)


visited = [False] * (NUMS)


# 순회 및 cnt
cnt = 0


def dfs(start_v, start=False):  # 산책중, 실내 만나면 끝
    global cnt

    if not start and is_internal_arr[start_v]:
        cnt += 1
        return

    visited[start_v] = True

    for child_v in graph[start_v]:
        if not visited[child_v]:
            dfs(child_v)

    #  백트래킹 주의
    visited[start_v] = False


for start_v in range(1, NUMS):
    if is_internal_arr[start_v]:
        dfs(start_v, start=True)

print(cnt)