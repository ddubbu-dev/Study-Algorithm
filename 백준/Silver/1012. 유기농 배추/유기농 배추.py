import sys
sys.setrecursionlimit(10**6)
readline = lambda: sys.stdin.readline().strip()
T = int(readline())
diff = [(-1, 0), (0, -1), (1, 0), (0, 1)]

def dfs(x, y):
    visited[x][y] = True

    for dx, dy in diff:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < M and 0 <= ny < N:
            if graph[nx][ny] and not visited[nx][ny]:
                visited[nx][ny] = True
                dfs(nx, ny)

def print_graph():
    for line in graph:
        print(line)


for _ in range(T):
    M, N, K = map(int, readline().split())
    graph = [[0] * N for _ in range(M)]  # matrix
    visited = [[False] * N for _ in range(M)]

    for _ in range(K):
        x, y = map(int, readline().split())
        graph[x][y] = 1

    all_visited = False
    round = 0

    while not all_visited:
        all_visited = True

        for y in range(N):
            for x in range(M):
                if graph[x][y] and not visited[x][y]:
                    all_visited = False
                    dfs(x, y)
                    round += 1
                    break
            if not all_visited:
                break

    print(round)
