import sys

readline = lambda: sys.stdin.readline().strip()

N = int(readline())
graph = []

for _ in range(N):
    graph.append(list(map(int, readline())))


def print_graph():
    for line in graph:
        print(line)


visited = [[False] * N for _ in range(N)]
diff = [(-1, 0), (0, -1), (1, 0), (0, 1)]


def dfs(x, y, cnt):  # TODO: 내부 요소 개수 세야함
    visited[x][y] = True
    cnt += 1

    for dx, dy in diff:
        nx = x + dx
        ny = y + dy

        if 0 <= nx < N and 0 <= ny < N:
            if graph[nx][ny] and not visited[nx][ny]:
                visited[nx][ny] = True
                cnt += dfs(nx, ny, 0)
    return cnt


all_visited = False
group_cnt = []

while not all_visited:
    for i in range(N):
        for j in range(N):
            if graph[i][j] and not visited[i][j]:
                cnt = dfs(i, j, 0)
                group_cnt.append(cnt)

    all_visited = True

print(len(group_cnt))
group_cnt.sort()

for cnt in group_cnt:
    print(cnt)