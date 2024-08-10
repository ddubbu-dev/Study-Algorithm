"""
[문제 이해]
- 9명 중 7명 키 합을 구해서 = 100인 경우 
- 난쟁이들 키 오름차순 출력

[풀이]
- 조합으로 9C7 경우의 수 찾기
"""

N = 9
arr = []
for i in range(N):
    arr.append(int(input()))

# 탐색 -
def make조합_중복없음(arr: list, cnt: int):
    result = []

    def inner(arr, start_idx, picked_arr):
        if len(picked_arr) == cnt:
            result.append(picked_arr)
            return
        for i in range(start_idx, len(arr)):
            inner(arr, i + 1, picked_arr[:] + [arr[i]])

    inner(arr, 0, [])

    return result



collections = make조합_중복없음(arr, 7)

for case in collections:
    acc = sum(case)

    if acc == 100:
        print("\n".join(map(str, sorted(case))))
        break