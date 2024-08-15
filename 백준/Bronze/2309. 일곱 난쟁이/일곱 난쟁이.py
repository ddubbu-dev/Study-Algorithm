from itertools import combinations

N = 9
nums = [int(input()) for _ in range(N)]


cases = combinations(nums, 7)


for case in cases:
    sorted_case = sorted(list(case))
    acc = sum(sorted_case)

    if acc == 100:
        for item in sorted_case:
            print(item)
        break
