
"""
Quick정렬 (w. 분할 정복 알고리즘, 재귀)

1. 방법
- 리스트를 2개의 sub 리스트로 분할 (mergeSort와 달리 pivot 기준으로 좌/우 쪼개기)
- sub리스트 size=1 될 때까지 분할 반복 = 정복 완료
- 참고, 한 턴이 끝나면, pivot 의 위치는 정해진다.

2. 시간 복잡도
[최선]
   | |
   | |  
   | |
   | |
    ↓  O(logN)  [1] 분할
                    - 순환 호출 깊이
                    - N 사이즈 리스트가 사이즈 1 sub리스트가 될때까지 분할하는 시간
       O(N)     [2] 비교 : 좌우 값 비교

[최악]
- 만약 pivot 을 잘못 잡아 제일 작거나 제일 클때, 분할이 되지 않음. 
- 일반 정렬 O(n^2) 과 같은 시간 복잡도를 가지게 됨

3. 공간 복잡도 O(logN)

"""

def quickSort(arr):
    if len(arr) <= 1:
        return arr

    pivot_idx = len(arr) // 2  # 임의로 가운데값
    pivot_val = arr[pivot_idx]

    left_arr = []  # less than pivot
    right_arr = []  # greater than pivot

    for num in arr:
        if num < pivot_val:
            left_arr.append(num)
        # 주의) 중복 수 없다는 가정하에, 있으면 다른 방법 필요!
        elif pivot_val == num:  
            continue
        else:
            right_arr.append(num)

    # 끝나면, arr[pivot] 위치는 고정됨
    return quickSort(left_arr) + [pivot_val] + quickSort(right_arr)


# =============== 함수 정의 끝 ===============
import sys


def cinput():
     return sys.stdin.readline().rstrip()


T = int(cinput())
arr = []

for i in range(T):
    num = int(cinput())
    arr.append(num)

sorted_arr = quickSort(arr)

for item in sorted_arr:
    print(item)
