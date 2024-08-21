"""
[문제 분석]
append: 타겟 번호보다 크면
pop: 타겟 번호이면 출력
(x) 타겟번호보다 작으면? -> 그럴 경우 "Sad" 불가능

[반례](https://www.acmicpc.net/board/view/137024)
- nums 순회 idx 별도 관리 필요함
"""

import sys

readline = input  # lambda: sys.stdin.readline().strip()


N = int(readline())
nums = list(map(int, readline().split()))

stack = []
target_n = 1
nums_idx = 0

while nums_idx < N:
    if stack and stack[-1] == target_n:
        stack.pop()
        target_n += 1
        continue

    num = nums[nums_idx]
    if num == target_n:
        target_n += 1
    elif target_n < num:
        stack.append(num)
    else:  # target_n > num
        print("Sad")
        exit()

    nums_idx += 1

for num in range(target_n, N + 1):
    stacked = stack.pop()

    if num != stacked:
        print("Sad")
        exit()

print("Nice")
