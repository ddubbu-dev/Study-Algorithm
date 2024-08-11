import sys
def input():
    return sys.stdin.readline().rstrip()


def print_dev_only(args):
    printable = False
    if printable:
        print(args)


division_by = 1_000


def multiply_matrix(A, B):
    result_M = []
    size = len(A)
    print_dev_only(f"A={A}\nB={B}")
    for row_1 in range(size):
        sub_list = []

        for col_2 in range(size):
            # 자릿수마다 곱해서 더해주기
            A_collected_w_row = A[row_1]
            B_collected_w_col = []

            for row_2 in range(size):
                B_collected_w_col.append(B[row_2][col_2])

            acc = 0
            for i in range(size):
                acc += A_collected_w_row[i] * B_collected_w_col[i]
            sub_list.append(acc % division_by)

        result_M.append(sub_list)
        # sub_list = multiply_matrix(A_collected_w_row, B_collected_w_col)
        # print_dev_only(sub_list)

        # result_M.append(sub_list)

    # print_dev_only(f"result={result_M}")
    return result_M


computed_storage = {}


def get_square_matrix(M, square):
    result = None

    if square == 1:  # 정복
        result = M
    elif computed_storage.get(square) != None:
        result = computed_storage.get(square)
    elif square % 2 == 0:  # 분할
        half_M = get_square_matrix(M, square // 2)
        result = multiply_matrix(half_M, half_M)
    else:
        reduced_M = get_square_matrix(M, (square - 1))
        result = multiply_matrix(reduced_M, M)

    computed_storage[square] = result

    return result


N, B = map(int, input().split())
matrix = []

for i in range(N):
    matrix.append(list(map(int, input().split())))


result = get_square_matrix(matrix, B)

for i in range(N):
    for j in range(N):
        print(result[i][j] % division_by, end=" ")
    print("")
