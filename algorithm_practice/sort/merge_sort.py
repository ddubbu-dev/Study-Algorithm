def set_open(input_):
    class open:
        def __init__(self, x):
            self.read = lambda: input_

        def __iter__(self):
            return iter(input_.split("\n"))

    return open


def set_input(input_):
    return iter(input_.split("\n")).__next__


input = set_input(
    """3
    3
    2
    1"""
)


### /////// 아래부터 제출 영역 ///////

"""
Merge정렬 (w. 분할 정복 알고리즘, 재귀)

1. 방법
- 리스트를 2개의 sub 리스트로 분할
- sub리스트들을 정렬한 다음
- sub리스트들을 하나로 합치면서, 전체가 정렬

2. 시간 복잡도

    ↑  O(N) [2] 병합 (이때, 두 리스트는 각각 정렬이 되어있다는 전제)
   | |
   | |  
   | |
   | |
    ↓  O(logN) [1] 분할
                    - N 사이즈 리스트가 사이즈 1 sub리스트가 될때까지 분할하는 시간
                    - 사이즈 1 sub 리스트, 정렬 문제 정복!
"""


def devideList(arr):
    size = len(arr)

    if size <= 1:
        return arr, []

    mid = size // 2
    return arr[:mid], arr[mid:]


def mergeList(A, B):  # 가정은,
    result = []

    point_a, point_b = 0, 0

    while point_a < len(A) and point_b < len(B):
        if A[point_a] <= B[point_b]:
            result.append(A[point_a])
            point_a += 1
        else:
            result.append(B[point_b])
            point_b += 1

    # 혹 한쪽 탐색이 끝났다면, 한꺼번에 붙이기
    if point_a >= len(A):
        result += B[point_b:]
        point_b = len(B)

    else:
        result += A[point_a:]
        point_a = len(A)

    return result


def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    A, B = devideList(arr)
    result = mergeList(mergeSort(A), mergeSort(B))

    return result


# =============== 함수 정의 끝 ===============

T = int(input())
arr = []

for i in range(T):
    num = int(input())
    arr.append(num)

sorted_arr = mergeSort(arr)


for item in sorted_arr:
    print(item)
