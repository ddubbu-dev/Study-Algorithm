"""
[참고자료](https://e-juhee.tistory.com/entry/python-%EB%B0%B1%EC%A4%80-11049-%ED%96%89%EB%A0%AC-%EA%B3%B1%EC%85%88-%EC%88%9C%EC%84%9C-DP)
"""
import sys

readline = lambda: sys.stdin.readline().strip()
# readline = input

# 1. 전처리
N = int(readline())
matrix = []
for _ in range(N):
    r, c = map(int, readline().split())
    matrix.append((r, c))

# dp[i][j] = i ~ j 번째 행렬 내 최소 연산수
dp = [[0 for _ in range(N)] for _ in range(N)]

for term in range(1, N):
    for start in range(N - term):
        end = start + term
        dp[start][end] = float("inf")

        # 분할 후 최소값 구하기
        for t in range(start, end):
            added_operations = matrix[start][0] * matrix[t][1] * matrix[end][1]
            tmp = dp[start][t] + dp[t + 1][end] + added_operations

            if tmp < dp[start][end]:
                dp[start][end] = tmp

print(dp[0][N - 1])