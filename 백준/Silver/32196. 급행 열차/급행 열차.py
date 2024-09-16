"""
[시도2]
- GPT 도움
- 변화분, 그리디, 정렬

[시도1]
- 운행시간 최소값 (그리디)
- Bi 클수록, Ai 작을수록
- 문제 이해 실패 : 각 역에서 운행시간을 K로 봄, 전체 라서 변화분을 봐야함
"""

import sys
readline = lambda: sys.stdin.readline().strip()

# 전처리
n, m, k, x, y = map(int, readline().split())
diff_after_setup = []  # 대피선 설치 시 운행 시간 변화
for i in range(n):
    a, b = map(int, readline().split())
    diff_after_setup.append(a * x - b * y)
diff_after_setup.sort()  # 변화가 작은수부터 오름차순

diff_sum = sum(diff_after_setup[:m])

print(k * (x + y) + diff_sum)
