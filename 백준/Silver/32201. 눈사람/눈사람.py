"""
[시도2]
dict 만들어서 서치 시간 줄이기 O(1) 

[시도1] 시간초과
- (시간초과 예상) N^2 = 10^10
- 그렇다고 table을 만들기에는 10^9 배열 크기 만들어도 될까?
"""

import sys
readline = lambda: sys.stdin.readline().strip()

# 전처리
N = int(readline())
before_arr = list(map(int, readline().split()))
after_arr = list(map(int, readline().split()))
after_rank_dict = {}

for rank in range(N):
    a_member = after_arr[rank]
    after_rank_dict[a_member] = rank

max_level_up = 0
people = []

for before_rank in range(N):
    member = before_arr[before_rank]
    after_rank = after_rank_dict[member]

    level_up = before_rank - after_rank
    if level_up > max_level_up:
        max_level_up = level_up
        people = [member]
    elif level_up == max_level_up:
        people.append(member)


print(" ".join(list(map(str, people))))
