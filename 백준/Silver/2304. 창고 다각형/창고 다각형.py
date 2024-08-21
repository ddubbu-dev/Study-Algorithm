"""
[아이디어]
- tallest 범위 (혹은 단일 막대기)를 기준으로
- 좌측 : 오름차순 (stack[-1] < new) pop 후 직사각형 너비 연산 / append new
- 우측 : 내림차순 (stack[-1] > new)
-- 좀 다른게 끝까지 가보기 전까지 제일 높은 곳을 모름
-- 오른쪽부터 역산!

[반례](https://www.acmicpc.net/board/view/85458)
- tallest_range 범위 연산 조심
"""

import sys

readline = lambda: sys.stdin.readline().strip()
N = int(readline())

bars = []
# 최대높이 범위
tallest = 0
tallest_x = []
for _ in range(N):
    x, h = map(int, readline().split())
    bars.append((x, h))

    if tallest == h:
        tallest_x.append(x)
    elif tallest < h:
        tallest = h
        tallest_x = [x]

# x 기준 정렬
tallest_x.sort()
bars.sort()


X_INDEX = 0
HEIGHT = 1
result = 0

left_bars = bars[: bars.index((tallest_x[0], tallest))]
right_bars = bars[bars.index((tallest_x[-1], tallest)) + 1 :]
right_bars.reverse()


def calc(bars, is_left, compare_x):
    global result
    stack = []

    for bar in bars:
        x, h = bar
        if not stack:
            stack.append(bar)
            continue
        if (is_left and x < compare_x) or (not is_left and x > compare_x):  # 좌측
            if stack[-1][HEIGHT] < h:
                start_x, height = stack.pop()
                width = abs(start_x - x)
                result += width * height
                stack.append(bar)
    # 잔량 처리
    if stack:
        start_x, height = stack.pop()
        x = compare_x
        width = abs(start_x - x)
        result += width * height


calc(left_bars, True, tallest_x[0])
calc(right_bars, False, tallest_x[-1])
tallest_range = abs(tallest_x[0] - tallest_x[-1]) + 1 if len(tallest_x) >= 2 else 1
result += tallest * tallest_range
print(result)
