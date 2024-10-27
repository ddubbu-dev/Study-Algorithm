"""
binary search
- target: min size of album
- condition: # album 개수, group 담을 수 있는 크기
- training: l->[size]<-r

반례: https://www.acmicpc.net/board/view/58000
"""

import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())
tracks = list(map(int, input().split()))

l = max(tracks)
r = sum(tracks)

best_size = sys.maxsize

while l <= r:
    size = (l + r) // 2

    cnt_album = 0
    tmp = 0
    for n in tracks:
        if tmp + n < size:
            tmp += n
        elif tmp + n == size:
            cnt_album += 1
            tmp = 0  # init
        else:
            cnt_album += 1
            tmp = n

    if tmp:
        cnt_album += 1

    if cnt_album <= M:  # 앨범수 늘려야해서, size 줄이기
        best_size = min(best_size, size)
        r = size - 1
    else:
        l = size + 1

print(best_size)
