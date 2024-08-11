# [참고 자료](https://hstory0208.tistory.com/entry/Python%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%B0%B1%EC%A4%80-9663%EB%B2%88-N-Queen)
# TODO: 베껴서 다시 풀어야함

INIT_VALUE = 0
N = int(input())
# map = [[False] * N for _ in range(N)]  # 주의) 같은 참조로 여러개 만들면 안됨!
# (최적화) 2D > 1D
# - y_pos_arr[x_pos] = y_pos; map[x_pos][y_pos] 에 퀸을 놓겠다.
# - 한편으로는 모두 다른 숫자를 갖고 있어야겠네
y_pos_arr = [INIT_VALUE] * N


def checkValidPos(target_x_pos):

    # 대각선 탐색
    for i in range(target_x_pos):
        is_in_same_line = y_pos_arr[target_x_pos] == y_pos_arr[i]
        is_in_same_cross = abs(y_pos_arr[target_x_pos] - y_pos_arr[i]) == abs(
            target_x_pos - i
        )

        if is_in_same_line or is_in_same_cross:
            return False

    return True


cnt = 0


def travel(x_pos):  # (0 >> N) 현재 x_pos 고정해서 위치 찾는 중
    global cnt
    if x_pos == N:
        cnt += 1  # 탈출 - 끝까지 도달 성공
        return

    for y_pos in range(N):
        y_pos_arr[x_pos] = y_pos
        valid = checkValidPos(x_pos)
        if valid:
            travel(x_pos + 1)


travel(0)
print(cnt)
