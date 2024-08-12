
"""
[작동 체크를 위한 좋은 입출력]
1 1 1 #3
2 3 3 #15
3 7 7 #63

[최적화]
- 방법1: memoization
모든 사분면을 반복하는게 아니라, 
1사분면만 알면 2~4사분면 중에 선택해서 바로 넘어갈 수 있음

- 방법2: 규칙성, 수식 찾기 (=> 문제보면 규칙이 있을지 고민 필요)
"""


N, r, c = map(int, input().split())

cnt = 0

while N != 0:
    N -= 1  # N번 연산으로 끝나다니
    size = pow(2, N)  # 위에서 미리 절반을 나눔으로써 half_size 의미 내재

    sub_area_cnt = pow(size, 2)
    if r < size and c >= size:  # 1사분면
        cnt += sub_area_cnt * 1
        c -= size
    elif r < size and c < size:  # 2사분면
        cnt += sub_area_cnt * 0
    elif r >= size and c < size:  # 3사분면
        cnt += sub_area_cnt * 2
        r -= size
    else:  # 4사분면
        cnt += sub_area_cnt * 3
        r -= size
        c -= size


print(cnt)


""""
[최적화 안된 기존 풀이]
"""

exit_now = False

# idx; size=2^idx일때 값
# (size-1, size-1) 방문값은 end_cnt
storage = []  # end_cnt 모음


def travel_w_history(size, start_x_pos, start_y_pos, cnt):
    # 팁
    # - 백트래킹을 위해 cnt는 global 값이 아님
    # - 출력만 하는거라 그냥 size로 관리
    global exit_now
    if exit_now:  # 이미 출력했으면 끝내기
        return

    # 정복
    if size == 2:
        for i in range(start_x_pos, start_x_pos + size):
            for j in range(start_y_pos, start_y_pos + size):
                print(f"size={size}, ({i},{j}), cnt={cnt}")
                if i == r and j == c:

                    print(cnt)
                    exit_now = True
                    return
                cnt += 1
        return

    # N = math.sqrt(size)  # ex. 3
    # if N <= len(storage):  # 분할; 최적화 가능
    #     # TODO

    # 분할; 사분면으로 쪼개기
    half_size = size // 2
    start_positions = [  # 주의) 시작 지점도 변수화 필요
        [start_x_pos, start_y_pos],
        [start_x_pos, start_y_pos + half_size],
        [start_x_pos + half_size, start_y_pos],
        [start_x_pos + half_size, start_y_pos + half_size],
    ]
    case_nums = len(start_positions)
    for idx in range(case_nums):  # i=N사분면
        [x, y] = start_positions[idx]
        travel_w_history(size // 2, x, y, cnt + pow(half_size, 2) * idx)
