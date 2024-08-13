"""
[문제 이해]
- (1D) y_pos_arr = []; y_pos_arr[x_pos] = y_pos # 퀸을 놓은 자리
- valid 수식 찾기 필요
- dfs, 백트래킹 중요!!
"""

N = int(input())
y_pos_arr = [-1] * N


used_cols = [True] * N
정방향_cross = [True] * (N << 1)  # 2N-1
역방향_cross = [True] * (N << 1)  # (최적화) 비트 연산자로 2배처리


def set_queen(x_pos, y_pos):
    y_pos_arr[x_pos] = y_pos
    정방향_cross[x_pos + y_pos] = False
    역방향_cross[x_pos - y_pos + N - 1] = False
    used_cols[y_pos] = False


def reset_queen(x_pos, y_pos):
    y_pos_arr[x_pos] = -1
    정방향_cross[x_pos + y_pos] = True
    역방향_cross[x_pos - y_pos + N - 1] = True
    used_cols[y_pos] = True

cnt = 0

def dfs(x_pos):
    # 주의) x_pos; depth 정의 필요! y_pos_arr 만으로 관리할 수 있다고 생각했음

    global cnt, y_pos_arr

    if x_pos == N:  # 탈출
        cnt += 1
        return

    for y_pos in range(N):
        if not (used_cols[y_pos] and 정방향_cross[x_pos + y_pos] and 역방향_cross[x_pos - y_pos + N - 1]):
            continue
            
        set_queen(x_pos, y_pos)
        dfs(x_pos + 1)
        reset_queen(x_pos, y_pos)


dfs(0)
print(cnt)
