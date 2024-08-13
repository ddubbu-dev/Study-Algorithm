
"""
[방법1]
- 단순히, arr.sort() 후 arr[0]++, action_cnt ++
- 시간초과

[방법2] binary_search target; end_idx
- binary_search 이건 어디에 쓰는건가?
-- 최소레벨이라 action을 취해줄 idx를 찾는 방법? 사실 가장 왼쪽거 올리면됨
-- 다만 어디까지 action을 취해줄까? 하는 end_idx를 찾는게; binary_search target 이라고 생각했음
-- condition; action_cnt <= K (이보다 적게 올릴 수 있음)
- 처음엔 action 취하고 다시 arr.sort 가 필요한가 했는데, 
- 앞에서부터 차근히 idx++ 해주면서 증가해줘서 불필요


[궁금한점]
- K만으로도 10초가 넘는 연산인데.. 단순히 action++ 은 어케해야하지..?

[방법3] 최적화 버전
- binary_search target; level
- condition; action_cnt <= K (이보다 적게 올릴 수 있음)
- 잠깐만... 어떻게 K 연산을 제거하지?? => 불필요해짐
"""


N, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]
arr.sort()

## 방법3

# level range
start = arr[0]
end = arr[-1] + K  # 최대 액션을 취했을 경우

best_level = 0


def get_action_cnt(level):
    action_cnt = 0
    for i in range(len(arr)):
        item = arr[i]
        if item >= level:
            break
        action_cnt += level - item

    return action_cnt


while start <= end:
    level = (start + end) // 2

    action_cnt = get_action_cnt(level)

    if action_cnt <= K:  # action_cnt++, level++
        best_level = max(level, best_level)
        start = level + 1
    else:
        end = level - 1


print(best_level)

## ================= 방법2 =================
# start_idx = 0
# action_cnt = 0
# best_level = 0


# def get_end_idx(start_idx, target):
#     # target과 같은 마지막 end_idx 를 찾아야함

#     end_idx = len(arr) - 1

#     while start_idx <= end_idx:
#         mid_idx = (start_idx + end_idx) // 2
#         mid = arr[mid_idx]
#         if target == mid:
#             return end_idx

#         if target <= mid:  # 왼쪽으로
#             end_idx = mid_idx - 1
#         else:  # 오른쪽으로
#             start_idx = mid + 1

#     return end_idx


# while action_cnt < K:
#     min_level = arr[start_idx]
#     end_idx = get_end_idx(start_idx, min_level)  # 여기가 binary_search

#     print(f"({start_idx}, {end_idx})", end=" ")

#     for i in range(start_idx, end_idx + 1):
#         if action_cnt >= K:
#             break  # 더 이상 액션 취할 수 없음

#         arr[i] = arr[i] + 1
#         action_cnt += 1

#     # arr.sort()  # 값 바뀌었음
#     print(f"cnt={action_cnt}, arr={arr}")


# print(min(arr))
