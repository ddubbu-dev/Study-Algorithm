
"""
[눈여겨볼 것]
Q. 왜 이진탐색을 써야하는가?
A. N=10^5, O(N^2)의 경우 100억 연산, 즉 100초가 걸린다. 
이에 O(N*logN)으로, 탐색 연산수를 줄여줘야한다.

[고도화 필요]
- 이진트리구조를 이용하고 싶었으나, 실패
- 우선 분할 정복으로 풀이
"""


N = int(input())
A = list(map(int, input().split()))
A.sort()
# 팁) 대소 규칙을 넣어, 좌/우 편하게 버리기 위함
# - 순간 A 기존 순서가 바뀌는 단점이 있다고 생각했는데, B를 순회하니깐 노 상관

M = int(input())
B = list(map(int, input().split()))


def binary_search(target, start_idx, end_idx):
    if start_idx == end_idx:
        if A[start_idx] == target:
            return True
        else:
            return False

    mid_idx = (start_idx + end_idx) // 2
    mid_item = A[mid_idx]

    if target <= mid_item:  # 좌 탐색
        return binary_search(target, start_idx, mid_idx)
    else:  # 우 탐색
        return binary_search(target, mid_idx + 1, end_idx)


size = len(A)
for item in B:
    if binary_search(item, 0, size - 1):
        print(1)
    else:
        print(0)
