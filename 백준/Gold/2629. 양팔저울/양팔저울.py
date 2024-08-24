"""
** hold 배낭 알고리즘
[무게 확인 가능법]
- 가벼운 구슬? (구슬+가벼운무게추)=무거운무게추
- 무거운구술? 구슬 = 가벼운무게추 누적합

** 채택 정답 풀이
[참고자료](https://my-coding-notes.tistory.com/157)
- 단순 무게가 아니라 인자 범위를 줄이네 > '추의 개수'별로 만들 수 있는 무게?


[참고자료2]
- 배낭문제로? https://namhyo00.tistory.com/31
- 무게 얹히는 3가지 그림으로 https://hseungyeon.tistory.com/354
"""
import sys

readline = lambda: sys.stdin.readline().strip()
readline = input

# 1. 전처리
weight_cnt = int(readline())
weights = list(map(int, readline().split()))
stone_cnt = int(readline())
stones = list(map(int, readline().split()))

# 2. tabluation (행: 추의 개수, 열: 만들려는 무게)
max_weight = 500
max_target_weight = weight_cnt * max_weight
dp = [[False for _ in range(max_target_weight + 1)] for _ in range(weight_cnt + 1)]


def dfs(idx, target_weight):
    if idx > weight_cnt:  # 범위 오바
        return
    if dp[idx][target_weight]:  # 이미 방문
        return

    # dp; 추 idx번째까지 이용해서 target_weight 만들 수 있음
    dp[idx][target_weight] = True

    # ___구슬___ vs ___추___
    new_weight = weights[idx - 1]
    dfs(idx + 1, target_weight)  # 추를 올리지 않음
    dfs(idx + 1, abs(target_weight - new_weight))  # 왼쪽에 추 놓기
    dfs(idx + 1, target_weight + new_weight)  # 오른쪽에 추 놓기


dfs(0, 0)

# 추를 다 사용해서 만들 수 있는 무게들
possible_weight = dp[weight_cnt]
for stone in stones:
    if stone > max_target_weight:
        print("N", end=" ")
    elif possible_weight[stone]:
        print("Y", end=" ")
    else:
        print("N")
