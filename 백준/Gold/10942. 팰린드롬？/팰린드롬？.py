import sys

readline = lambda: sys.stdin.readline().strip()
# readline = input

# 1. 전처리
N = int(readline())
nums = list(map(int, readline().split()))
M = int(readline())


def print_dp(dp):
    for line in dp:
        print(line)


# dp[i][j] = nums[i] ~ nums[j] 팰린드롬 여부 저장
dp = [[0 for _ in range(N)] for _ in range(N)]

# 초기화
for num_len in range(N):
    for start in range(N - num_len):
        end = start + num_len
        if start == end:  # 문자 1개
            dp[start][end] = 1
        elif nums[start] == nums[end]:
            if start + 1 == end:
                dp[start][end] = 1
            elif dp[start + 1][end - 1]:
                dp[start][end] = 1


for _ in range(M):
    start, end = map(int, readline().split())
    print(dp[start - 1][end - 1])