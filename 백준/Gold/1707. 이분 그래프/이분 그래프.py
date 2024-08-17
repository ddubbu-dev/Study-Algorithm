"""
[참고자료](https://e-juhee.tistory.com/entry/python-%EB%B0%B1%EC%A4%80-1707-%EC%9D%B4%EB%B6%84-%EA%B7%B8%EB%9E%98%ED%94%84?category=1097015)
- 처음에, 자신 A / 인접한 노드 B 그룹 분리
-- 이때, 상대 그룹에 이미 들어가 있으면, error!
- 인접노드 마찬가지로 dfs 탐색


[아이디어]
- 그룹을 flag로 관리했네..

[반례1](https://www.acmicpc.net/board/view/136442)
[반례2](https://www.acmicpc.net/board/view/107653)
- 시작 노드와 이미 동떨어진 그래프들 > 끊어졌을 수 있으니; 전체 노드를 각 시작점으로 순회해보기
"""

import sys
readline = lambda : sys.stdin.readline().strip()
sys.setrecursionlimit(10**9)

K = int(readline())
NO_VISIT = 0
GROUP_A = -1
GROUP_B = 1
GROUP_TEMP_0 = 3


def dfs(graph, start_v, visited, start_group):
    visited[start_v] = start_group

    for child_v in graph[start_v]:
        if visited[child_v] == NO_VISIT:
            # 주의: 재귀 결과값 체크 필요함
            valid = dfs(graph, child_v, visited, -start_group)
            if not valid:
                return False
        elif visited[child_v] == start_group:
            return False
    return True


for _ in range(K):
    # 그래프 생성
    V, E = map(int, readline().split())
    graph = [[] for _ in range(V + 1)]

    for _ in range(E):
        u, v = map(int, readline().split())

        graph[u].append(v)
        graph[v].append(u)

    visited = [NO_VISIT] * (V + 1)
    visited[0] = GROUP_TEMP_0  # 임시

    valid = True
    # 끊어졌을 수 있으니; 전체 노드로 시작해보기!
    for start_v in range(1, V + 1):
        if visited[start_v] == NO_VISIT:
            valid = dfs(graph, start_v, visited, GROUP_A)  # 1부터, GROUP_A 부터 시작해도 무관

            if not valid:
                break

    if valid:
        print("YES")
    else:
        print("NO")
