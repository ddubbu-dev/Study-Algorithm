import sys
def input():
    return sys.stdin.readline().rstrip()

N = int(input())
nums = list(map(int, input().split()))
nums.sort()

M = int(input())
targets = map(int, input().split())


def check_is_in(target: int):
    l = 0
    r = len(nums) - 1

    while l <= r:
        mid = (l + r) // 2

        if nums[mid] == target:
            return 1
        elif nums[mid] < target:
            l = mid + 1
        else:
            r = mid - 1

    return 0


for target in targets:  # O(10^5)
    print(check_is_in(target))  # O(log(10^5)) 으로 줄여야함
