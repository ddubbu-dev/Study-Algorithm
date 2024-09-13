"""
[풀이]
- 대각선 i번째 구하기
- i 홀수? 왼쪽 끝부터 (i/1) > (i--/1++) distance 만큼
- i 짝수? 오른쪽 끝부터 (1/i) > (1++/i--) distance 만큼
"""

import sys

readline = lambda: sys.stdin.readline().strip()
readline = input

target_num = int(readline())

# get (좌 or 우) 끝 번호
cross_idx = 1
end_num = 1
while end_num < target_num:
    cross_idx += 1
    end_num += cross_idx

# 거리만큼 이동 후 분수 구하기
distance = end_num - target_num
if cross_idx % 2 == 0:
    denominator = cross_idx
    numerator = 1

    while distance:
        distance -= 1
        denominator -= 1
        numerator += 1
else:
    denominator = 1
    numerator = cross_idx

    # distance 만큼 이동해서 분수 구하기
    distance = end_num - target_num
    while distance:
        distance -= 1
        denominator += 1
        numerator -= 1


print(f"{denominator}/{numerator}")
