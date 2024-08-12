"""
[시간 복잡도 분석] 
O(NxM) = 10^6 x 2 x 10^10 =10^16
=> 말이 안됨 1초에 1억 연산 훨씬 뛰어넘음..!
=> 최대한 승수를 낮추기 위해, O(N x log(M)) 
=> 나무 높이쪽을 binary search 해야함

[이럴때 binary search를 하는군]
- 최적의 값을 찾아감
- 예시) 누적합 ↓, height ↑ 방향으로 학습시키기
"""

N, M = map(int, input().split())
trees = list(map(int, input().split()))
trees.sort(reverse=True)  # 내림차순 정렬
# TODO: 최적화해볼수도? 더 이상 remain 없으면 sum 그만두기

max_height = max(trees)
# heights = list(range(max_height, -1, -1))

prev_candidate_height = -1


def get_remains(height):
    acc = 0
    for tree in trees:
        if tree > height:
            acc += tree - height

    return acc


def binary_search(
    start_idx,
    end_idx,
):

    global prev_candidate_height
    if start_idx > end_idx:
        return

    if start_idx == end_idx:
        height = max_height - start_idx
        if get_remains(height) >= M:  # 후보 아니면, 갱신 못함
            if height > prev_candidate_height:
                prev_candidate_height = height
        return

    mid_idx = (start_idx + end_idx) // 2
    height = max_height - mid_idx
    acc = get_remains(height)

    # binary search 시작; (좌/우 이동 기준) 재밌음
    if acc >= M:  # acc ↓, height ↑
        # 아직 충분히 많이 잘랐으니, 덜 자르는 쪽으로
        # 다만, 갱신은 요구사항보다 큰 값일때
        if height > prev_candidate_height:
            prev_candidate_height = height
        binary_search(start_idx, mid_idx)
    else:  # acc ↑, height ↓
        binary_search(mid_idx + 1, end_idx)


binary_search(0, max_height)
print(f"{prev_candidate_height}")
