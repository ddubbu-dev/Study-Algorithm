"""
최고의 인재만을! 그리디 알고리즘 예상..
"""

import sys

readline = lambda: sys.stdin.readline().strip()
# readline = input

# 전처리
T = int(readline())
LAST_SCORE = 100_000

for _ in range(T):
    N = int(readline())
    members = []
    for _ in range(N):
        # 성적 순위
        a, b = map(int, readline().split())
        members.append((a, b))

    members.sort()  # 순위가 낮을수록 잘하는 사람

    cnt = 0
    best_a, best_b = LAST_SCORE, LAST_SCORE

    for a, b in members:
        if best_a >= a or best_b >= b:
            cnt += 1
            best_a = min(best_a, a)
            best_b = min(best_b, b)

    print(cnt)