"""
[시간초과]
- 최소로 취할 값 x 개수 => 최대치 저장해두기
- 최소는 N마다 갱신될 수 있어서 O(N^2=10^10) > 2초;

[정답풀이]
- 만약 ropes가 내림차순이라면? idx자체가 곧 자기보다 큰 요소의 개수!
-- 그럼 O(nlog(n)) 까지 최적화 가능
- Greedy 는 사전처리 Greedy 조건을 만드는게 중요한 것 같다.
"""

import sys

readline = lambda: sys.stdin.readline().strip()

# 전처리
n = int(readline())
ropes = []
for _ in range(n):
    ropes.append(int(readline()))
ropes.sort(reverse=True)

max_weight = 0
for idx, rope in enumerate(ropes):
    weight = rope * (idx + 1)
    max_weight = max(max_weight, weight)

print(max_weight)
