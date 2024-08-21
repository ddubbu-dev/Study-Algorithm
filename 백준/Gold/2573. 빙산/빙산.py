import sys
sys.setrecursionlimit(10**6)
readline = lambda: sys.stdin.readline().strip()

N, M = map(int, readline().split())
graph = []

for _ in range(N):
    line = list(map(int, readline().split()))
    graph.append(line)

diff = [(-1, 0), (0, -1), (1, 0), (0, 1)]


def dfs(x, y):
    visited[x][y] = True

    ice_cnt = 0

    for dx, dy in diff:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < N and 0 <= ny < M:
            if graph[nx][ny] == 0:
                ice_cnt += 1
            elif graph[nx][ny] and not visited[nx][ny]:
                visited[nx][ny] = True
                dfs(nx, ny)

    melt_candidate.append((x, y, ice_cnt))


def search_vertex():
    for x in range(N):
        for y in range(M):
            if graph[x][y]:
                return (x, y)
    return None


def find_no_visit_vertex():
    for x in range(N):
        for y in range(M):
            if graph[x][y] and not visited[x][y]:
                return True
    return False


def print_graph():
    for line in graph:
        print(line)


years = 0
while True:

    # 1. 순회하면서, 녹게될 빙산 후보지 리스트업
    melt_candidate = []  # (x, y, cnt)

    # 2. 순회 및 빙산 분리 체크
    visited = [[False] * M for _ in range(N)]
    vertex = search_vertex()

    if vertex:
        dfs(vertex[0], vertex[1])
        if find_no_visit_vertex():  # 빙산 분리됨
            print(years)
            exit()
    else:  # 다 녹아버림
        print(0)
        exit()

    # 3. 녹이기
    for x, y, cnt in melt_candidate:
        graph[x][y] = max(graph[x][y] - cnt, 0)  # 0 이상으로 설정되도록

    years += 1
