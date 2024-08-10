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

def get순열_중복없음(storage_nums, k, picked_nums, search_idx):
    collections = []  # 값 생성을 위해 클로저 정의

    def recur(picked_nums, search_idx):
        if search_idx >= len(storage_nums):
            return

        if len(picked_nums) == k:  # 재귀 - 탈출
            collections.append(picked_nums[:])  # 주의) 리스트 참조값
            return

        picked_num = storage_nums[search_idx]

        if storage_nums[search_idx] not in picked_nums:
            picked_nums.append(picked_num)
            recur(picked_nums, 0)

            # 재귀 - 복구
            picked_nums.pop()

        # 재귀 - 호출
        recur(picked_nums, search_idx + 1)  # 그 다음부터 찾기

    recur(picked_nums, search_idx)
    return collections


collections = get순열_중복없음(arr, 7, [], 0)

for case in collections:
    acc = sum(case)

    if acc == 100:
        print("\n".join(map(str, sorted(case))))
        break