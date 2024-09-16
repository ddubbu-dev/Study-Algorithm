"""
[시도1]
- 오름차순 정렬 후 그리디
- 마지막 2개 항상 치우기(값-1) / (0 되면 pop)
- 한개 남으면 마찬가지
- 혹시 times 혹은 item_time > 1440 이면, break
"""

import sys
readline = lambda: sys.stdin.readline().strip()

# 전처리
n = int(readline())
houses = list(map(int, readline().split()))
houses.sort()


LIMIT_TIME = 1440
times = 0
while True:
    if times > LIMIT_TIME:
        print(-1)
        break
    if len(houses) == 0:
        print(times)
        break
    if len(houses) == 1:
        times += houses[-1]
        if times > LIMIT_TIME:
            print(-1)
        else:
            print(times)
        break
    else:
        times += 1
        houses[-1] -= 1
        houses[-2] -= 1

        if houses[-2] == 0:
            last_item = houses.pop()
            houses.pop()
            if last_item > 0:
                houses.append(last_item)
                houses.sort()  # 다시 정렬
