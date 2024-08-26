"""
- Bottom-Up
- [실패] 과거값으로 갱신 시 step_1 몇번을 통해 도달했는지 저장이 안됨
- [정답풀이](https://velog.io/@hyuntall/%EB%B0%B1%EC%A4%80-2579%EB%B2%88-%EA%B3%84%EB%8B%A8-%EC%98%A4%EB%A5%B4%EA%B8%B0-%EB%AC%B8%EC%A0%9C-%ED%92%80%EC%9D%B4-%ED%8C%8C%EC%9D%B4%EC%8D%AC)
- [실패2] 점화식 범위 외 예외처리
"""

import sys

readline = lambda: sys.stdin.readline().strip()
# readline = input

# 1. 전처리
N = int(readline())
arr = [0]  # 출발점 초기화
for _ in range(N):
    arr.append(int(readline()))

# dp[i] = i번째 도달 시 최대 점수
dp = [0] * (N + 1)
# init
dp[0] = 0
dp[1] = arr[1]

if N == 1:
    print(dp[-1])
    exit()

dp[2] = arr[1] + arr[2]  # 놓친 부분

for i in range(1, N + 1):
    if i - 2 >= 0:
        dp[i] = max(dp[i], dp[i - 2] + arr[i])
    if i - 3 >= 0:
        dp[i] = max(dp[i], dp[i - 3] + arr[i - 1] + arr[i])

print(dp[-1])
