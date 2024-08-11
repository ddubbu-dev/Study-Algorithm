
"""
[문제 이해]
- 단순 연산으로 보이지만, 제곱승수 B <= 2,147,483,647 임을 감안해야함
- Q. 이걸 어떻게 분할정복하지?? A. 아이디어가 필요함.. 흐음..

[수식]
- 짝수, C^n = C^(n/2)*C^(n/2)
- 홀수, C^(n-1) = C * C^((n-1)/2)*C^((n-1)/2)

[개선해볼 것]
- 미리 계산된 승수는 미리 저장해도 되지 않을까?
"""

A, B, C = map(int, input().split())
EMPTY_VALUE = 0
square_dict = {0: 1}  # [1] + [EMPTY_VALUE] * MAX_VALUE


def get_square_number(num, square):
    result = None

    if square == 0:  # 정복
        result = square_dict[square]
    elif square == 1:
        result = num
    elif square_dict.get(square) != None:  # 계산 최적화
        result = square_dict[square]
    elif square % 2 == 0:  # 분할
        half = get_square_number(num, square // 2)
        result = half * half
    else:
        half = get_square_number(num, (square - 1) // 2)
        result = half * half * num

    # 계산 최적화
    result = result % C
    square_dict[square] = result

    return result  # 크기 최적화


result = get_square_number(A, B)
print(result % C)
