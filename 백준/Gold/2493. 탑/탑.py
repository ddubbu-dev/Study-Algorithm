
from collections import deque

# import sys
# readline = lambda: sys.stdin.readline().strip()
readline = input

stack = deque()

N = int(input())
arr = list(map(int, input().split()))  # Q. 메모리 제한 괜찮을까? 이건 읽는 문제 인듯

for idx in range(1, len(arr) + 1):
    num = arr[idx - 1]

    if len(stack) == 0:
        stack.append((num, idx))
        print(0, end=" ")
        continue

    high_top_num, high_top_idx = stack[-1]  # 왼쪽에서 가장 높은 수신탑
    if high_top_num >= num:
        print(high_top_idx, end=" ")
        stack.append((num, idx))
    else:
        while True:
            try:
                if stack[-1][0] < num:
                    stack.pop()
                    continue
                else:
                    high_top_num, high_top_idx = stack[-1]  # 왼쪽에서 가장 높은 수신탑
                    print(high_top_idx, end=" ")
                    stack.append((num, idx))
                    break
            except:
                stack.append((num, idx))
                print("0", end=" ")
                break
