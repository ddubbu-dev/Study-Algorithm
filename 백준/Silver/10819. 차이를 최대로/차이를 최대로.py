def make_순열_중복없음(arr: list, cnt: int):
    result = []

    def inner(arr, picked_arr):
        if len(picked_arr) == cnt:
            result.append(picked_arr)
            return

        for i in range(0, len(arr)):
            if not arr[i] in picked_arr:
                inner(arr, picked_arr[:] + [arr[i]])

    inner(arr, [])

    return result
N = int(input())
arr = list(map(int, input().split()))

cases = make_순열_중복없음(range(len(arr)), N)

max_v = 0
for idxes in cases:
    acc = 0
    for i in range(len(idxes) - 1):
        acc += abs(arr[idxes[i]] - arr[idxes[i + 1]])

    if acc > max_v:
        max_v = acc

print(max_v)
