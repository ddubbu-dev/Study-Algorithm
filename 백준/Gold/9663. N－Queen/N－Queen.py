"""
[문제 이해]
- (1D) y_pos_arr = []; y_pos_arr[x_pos] = y_pos # 퀸을 놓은 자리
- valid 수식 찾기 필요
- dfs, 백트래킹 중요!!
"""

N = int(input())
y_pos_arr = [-1] * N


정방향_cross = [True] * ((2 * N) - 1)  # i + j
역방향_cross = [True] * ((2 * N) - 1)  # i - j + N - 1


def check_is_정방향_cross(x_pos, y_pos):
    return 정방향_cross[x_pos + y_pos]


def check_is_역방향_cross(x_pos, y_pos):
    return 역방향_cross[x_pos - y_pos + N - 1]


def set_queen(x_pos, y_pos):
    정방향_cross[x_pos + y_pos] = False
    역방향_cross[x_pos - y_pos + N - 1] = False
    y_pos_arr[x_pos] = y_pos


def reset_queen(x_pos, y_pos):
    정방향_cross[x_pos + y_pos] = True
    역방향_cross[x_pos - y_pos + N - 1] = True
    y_pos_arr[x_pos] = -1


def check_valid_pos(x_pos, y_pos):
    # 열 중복
    if y_pos in y_pos_arr:
        return False

    # 대각선 중복
    if check_is_정방향_cross(x_pos, y_pos) and check_is_역방향_cross(x_pos, y_pos):
        return True

    return False


cnt = 0


def dfs(x_pos):
    # 주의) x_pos; depth 정의 필요! y_pos_arr 만으로 관리할 수 있다고 생각했음

    global cnt, y_pos_arr

    if x_pos == N:  # 탈출
        cnt += 1
        return

    for y_pos in range(N):
        if check_valid_pos(x_pos, y_pos):
            set_queen(x_pos, y_pos)
            dfs(x_pos + 1)
            reset_queen(x_pos, y_pos)


dfs(0)
print(cnt)
