"""
[참고자료](https://velog.io/@ledcost/%EB%B0%B1%EC%A4%80-9252-%ED%8C%8C%EC%9D%B4%EC%8D%AC-LCS-2-%EA%B3%A8%EB%93%9C-4-DP)
"""
import sys

readline = lambda: sys.stdin.readline().strip()
readline = input

# 1. 전처리
line1 = readline()
line2 = readline()

# 과거값 비교를 위해 N+1만큼 사이즈를 잡아줌
dp = [["" for _ in range(len(line2) + 1)] for _ in range(len(line1) + 1)]


def print_dp():
    for line in dp:
        print(line)


for i in range(1, len(line1) + 1):
    for j in range(1, len(line2) + 1):
        s1 = line1[i - 1]
        s2 = line2[j - 1]

        if s1 == s2:
            dp[i][j] = dp[i - 1][j - 1] + s1  # or s2
        else:
            if len(dp[i - 1][j]) >= len(dp[i][j - 1]):
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i][j - 1]

lcs = dp[-1][-1]
print(len(lcs))
if lcs:
    print(lcs)
