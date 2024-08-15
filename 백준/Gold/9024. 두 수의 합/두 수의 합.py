"""
[이분 탐색]
target; n의 범위? arr[0] ~ arr[-1] => 끝점끼리 더하도록
condition; K랑 가깝도록

[틀린 이유]
- 고칠점, distance로 바꿔야함

"""


# best_sum 필요한지 고민됨
def binary_search(arr, K):
    best_distance, cnt = float("inf"), 0

    start_idx = 0
    end_idx = len(arr) - 1

    def move_pointer(K, _sum, start_idx, end_idx):
        if K > _sum:  # _sum ++
            start_idx += 1
        else:  # _sum --
            end_idx -= 1

        return start_idx, end_idx

    while start_idx < end_idx:
        _sum = arr[start_idx] + arr[end_idx]
        d = abs(K - _sum)

        if d < best_distance:
            cnt = 1  # reset
            best_distance = d
            start_idx, end_idx = move_pointer(K, _sum, start_idx, end_idx)

        elif d == best_distance:
            cnt += 1
            start_idx, end_idx = move_pointer(K, _sum, start_idx, end_idx)

        else:  # d > best_distance
            start_idx, end_idx = move_pointer(K, _sum, start_idx, end_idx)

    return cnt


T = int(input())


for i in range(T):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    cnt = binary_search(arr, K)
    print(cnt)
