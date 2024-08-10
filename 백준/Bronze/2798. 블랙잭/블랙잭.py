"""
[문제 이해]
- 카드 합 21 이내, 합 최대
- (N)C(3) -> M을 넘지않으면서 최대값
- 이때의 카드 3장의 합
"""

import sys
from itertools import combinations 

def cinput():
    return sys.stdin.readline().rstrip()

N, M = map(int, cinput().split())
arr = map(int, cinput().split())

sum_max = 0

# 추후 필요 시 내장 함수 구현하기
for cards in combinations(arr, 3):
    sum_temp = sum(cards)
    
    if sum_temp <= M and sum_temp > sum_max:
        sum_max = sum_temp
        
print(sum_max)
