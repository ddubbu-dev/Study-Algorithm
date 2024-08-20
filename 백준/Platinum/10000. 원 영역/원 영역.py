"""
[유사 문제]
- 철로 라고 하는데, 공감 못함

[참고 자료](https://polohee81.tistory.com/51)
- 괄호문제로 해석하는게 신기하다

[나의 해석]
- stack에 들어있는 _OPEN 은 부모 영역

[반례 모음]
- https://www.acmicpc.net/board/view/113385
"""
import sys
readline = lambda: sys.stdin.readline().strip()
# readline = input

from collections import deque

_OPEN = "("
_CLOSE = ")"

T = int(readline())
spots = []
for _ in range(T):
    x, r = map(int, readline().split())
    spots.append((x - r, _OPEN))  # 왼쪽점
    spots.append((x + r, _CLOSE))  # 오른쪽점


# 주의, 닫히는 기호 먼저
spots.sort(key=lambda x: (x[0], -ord(x[1])))

CONNECTED = 1
NO_CONNECTED = 0

answer = 0
stack = deque()
for ptr in range(len(spots)):
    x, bracket = spots[ptr]

    if bracket == _OPEN:

        if len(stack) > 0:
            prev = stack[-1]
            prev_x = prev[0]
            if prev_x == x:  # 인접하므로, 연결 유지
                stack[-1] = (prev[0], prev[1], CONNECTED)

        stack.append((x, bracket, NO_CONNECTED))
        continue

    # _CLOSE
    prev_x, prev_bracket, prev_area = stack.pop()
    answer += prev_area + 1
    if ptr + 1 < len(spots):
        next_x = spots[ptr + 1][0]
        if x == next_x:
            continue
        else:  # 떨어진거임
            if len(stack) > 0:
                prev = stack[-1]
                stack[-1] = (prev[0], prev[1], NO_CONNECTED)

OUTER_AREA = 1
print(answer + OUTER_AREA)
