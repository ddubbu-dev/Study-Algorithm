N = int(input())
G = []

for _ in range(N):
    line = input().rstrip()
    line = list(map(int, line.split()))
    G.append(line)

blue = 0
white = 0


def dq(x, y, size):
    global blue, white

    if size == 0:
        return

    color = G[x][y]

    for i in range(x, x + size):
        for j in range(y, y + size):
            if color == G[i][j]:
                continue

            # 분할
            half_size = size // 2
            dq(x, y, half_size)
            dq(x + half_size, y, half_size)
            dq(x, y + half_size, half_size)
            dq(x + half_size, y + half_size, half_size)
            return  # 재귀 언제 복귀할지 조심하자

    if color == 1:
        blue += 1
    else:
        white += 1


dq(0, 0, N)


print(f"{white}\n{blue}")