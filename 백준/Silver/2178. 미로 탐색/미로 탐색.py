"""
Q. 사실 완전 탐색이라 DFS이면 안되나?
Q. graph 값을 업데이트하면서 이동하자!
Q. 왜 먼저 방문처리를 해줘야 시간초과가 안나지..? 더 알아봐야함
--> https://www.acmicpc.net/board/view/85576
"""

from collections import deque
import sys
readline = lambda : sys.stdin.readline().strip()
sys.setrecursionlimit(10**9)

# 그래프 만들기
IS_ROAD = 1
N, M = map(int, readline().split())
graph = []  # 열 값은 각각 만들 예정
for _ in range(N):
    line = [int(c) for c in readline()]
    graph.append(line)


# BFS 순회
diff_cases = [(0, 1), (1, 0), (0, -1), (-1, 0)]

visited = []
for _ in range(N):
    visited.append([False] * M)

que = deque([(0, 0)])  # (1, 1) 인덱스 주의


def print_matrix(cur_node):

    print(f"cur_node={cur_node}")
    for row in range(N):
        print(graph[row])
    print("====================")


def bfs():

    while que:
        x, y = que.popleft()
        # print_matrix((x, y))

        for dx, dy in diff_cases:
            new_x = x + dx
            new_y = y + dy

            # 인덱스 범위 내
            if 0 <= new_x <= N - 1 and 0 <= new_y <= M - 1:
                # 유효한 길
                if not visited[new_x][new_y] and graph[new_x][new_y] == IS_ROAD:
                    visited[new_x][new_y] = True
                    graph[new_x][new_y] = graph[x][y] + 1
                    que.append((new_x, new_y))


bfs()
print(graph[N - 1][M - 1])
