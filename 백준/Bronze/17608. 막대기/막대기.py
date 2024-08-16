
"""
[아이디어] 
- stack[-1] 보다 큰값이 들어오면, 그 안에 얘들 다 버리기
- 값 출력을 위해 (idx, value) tuple 로 저장하기
- 최종적으로 idx 만 출력하기
"""

from collections import deque

import sys
readline = lambda: sys.stdin.readline().strip()

N = int(readline())
stack = deque(maxlen=N)


for idx in range(1, N + 1):
    num = int(readline())

    if len(stack) == 0:
        max_v = num
        stack.append((idx, num))
        continue

    # 제일 크거나 같으면, 앞에거 다 버리고 최신 것만 유지
    while True:
        try:
            _, last_v = stack[-1]

            if last_v <= num:
                stack.pop()
            else:
                break
        except:
            break

    stack.append((idx, num))


print(len(stack))
