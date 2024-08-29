"""
[시간] 10~10:15 (삽질 10분)
[문제분석] a, b, c는 숫자가 아니라 max 범위
"""


import sys

sys.setrecursionlimit(10**6)
readline = lambda: sys.stdin.readline().strip()
# readline = input  # TODO: 백준 제출 시 제거하기

T = int(readline())

for _ in range(T):
    a, b, c = list(map(int, readline().split()))

    cnt = 0
    for x in range(1, a + 1):
        for y in range(1, b + 1):
            for z in range(1, c + 1):
                condition1 = x % y == y % z
                condition2 = y % z == z % x

                if condition1 and condition2:
                    cnt += 1

    print(cnt)
