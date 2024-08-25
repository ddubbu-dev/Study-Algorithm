"""
[고민해보기]
뽑는 순서
- 사용 횟수 적은걸 뽑기
- 곧 다가올 순서가 있다면 그대로 두기

[정답풀이1](https://magentino.tistory.com/88)
[원리] 페이징 기법 중 가장 낮은 빈도 데이터를 우선적으로 교체하는 belady's min algorithm

[정답풀이2](https://eunsun-zizone-zzang.tistory.com/79)
"""

import sys

readline = lambda: sys.stdin.readline().strip()
# readline = input

# 1. 전처리
N, K = map(int, readline().split())
items = list(map(int, readline().split()))


if N >= K:  # 콘센트 넉넉하면
    print(0)
    exit()

plug = []
cnt = 0  # 뽑는 횟수
MAX_ACTION = 101

for item_idx, item in enumerate(items):
    if item in plug:
        continue
    elif len(plug) < N:
        plug.append(item)
        continue

    priority = []
    for plugged_item in plug:
        remain_items = items[item_idx:]
        if plugged_item in remain_items:  # 다음에 또 사용해야한다면
            priority.append(remain_items.index(plugged_item))  # 그 다음 순서 대기
        else:  # 다음에 사용 안한다면
            priority.append(MAX_ACTION)

    # 우선순위 낮은거 제거하고, 새로 꽂아주기
    remove_idx = priority.index(max(priority))
    plug.remove(plug[remove_idx])
    plug.append(item)
    cnt += 1

print(cnt)
