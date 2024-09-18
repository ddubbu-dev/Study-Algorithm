"""

[시도1] 시간초과
- 놓고/안놓고 Bruthe Force 
- 원인: O(2^n) 연산 횟수.. 

[시도2] sub problem 정의 후 dp
"""

import sys
readline = lambda: sys.stdin.readline().strip()

# 전처리
n = int(readline())
SIZE = n + 1
dp_end_zero = [0] * (SIZE)  # 0으로 끝나는
dp_end_zero[1] = 0
dp_end_one = [0] * (SIZE)  # 1로 끝나는
dp_end_one[1] = 1

for i in range(2, SIZE):
    dp_end_zero[i] = dp_end_zero[i - 1] + dp_end_one[i - 1]
    dp_end_one[i] = dp_end_zero[i - 1]

print(dp_end_one[n] + dp_end_zero[n])
