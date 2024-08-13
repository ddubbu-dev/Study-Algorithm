
"""
[문제 이해]
- 양의 정수 (산성 용액) vs 음의 정수 (알칼리성 용액)
- binary_search target; 합칠 범위 : 오름차순, 최소값 ~ 최대값 
- condition; mixed => 0에 가까울수록
"""

N = int(input())
arr = list(map(int, input().split()))
arr.sort()

best_mixed = float("inf")
best_candidate = []

start_idx = 0
end_idx = len(arr) - 1


def move_left(mid_idx):
    global end_idx
    end_idx = end_idx - 1


def move_right(mid_idx):
    global start_idx
    start_idx = start_idx + 1


while start_idx < end_idx:

    start = arr[start_idx]
    end = arr[end_idx]

    mixed = start + end
    if abs(mixed) < abs(best_mixed):  # 같으면 한번만 출력
        best_mixed = mixed
        best_candidate = [start, end]

    # mixed (down)
    # range=(start, end)
    # - 0보다 오른쪽에 치우쳤으면, 왼쪽으로 보내고
    # - 0보다 왼쪽에 치우쳤으면, 오른쪽으로 보내고
    mid_idx = (start_idx + end_idx) // 2

    if start == 0 and end == 0:
        break
    elif start >= 0 and end > 0:
        move_left(mid_idx)
    elif start < 0 and end <= 0:
        move_right(mid_idx)
    else:  # start < 0 and end > 0:
        if abs(start) >= abs(end):
            move_right(mid_idx)
        else:
            move_left(mid_idx)

    # mixed (up)
    # 계속 낮아지는 것만 추구, 이미 위쪽에서 충분히 binary_search 진행 중

best_candidate.sort()
print(*best_candidate)
