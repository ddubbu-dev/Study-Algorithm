"""
[점화식 이해]
S(k) = S(k-1) + 'm' + 'o'*(k+2) + S(k-1) # 결과 점화식 
L(k) = 2*L(k-1) + k + 3, L(0) = 3 # 길이 점화식


[문제 이해]
- 무한히 만들되, N번째 길이까지 만들어졌으면 끝

[실패]
- (구현x) 재귀를 안돌고 k=0 에서 끝남
- (메모리 초과) 수열 찾은 뒤 N번째

[푸는 방법]
- 문자열 규칙을 찾아 바로 계산하기
- (v) length를 이용해보자! 코치님 코드 참고함
"""

s_0 = "moo"


def find_length(k):
    if k == 0:
        return len(s_0)
    return 2 * find_length(k - 1) + k + 3


def find_char(n):  # idx=N-1 위치의 값을 바로 찾기
    if n < 4:
        return s_0[n - 1]

    # n 길이에 맞는 k 먼저 찾기
    k = 0
    cur_length = find_length(k)
    while cur_length < n:  # 등호 없는 이유; n - 1
        k += 1
        cur_length = find_length(k)

    prev_length = find_length(k - 1)

    if n == prev_length + 1:
        return "m"
    elif n <= prev_length + 3 + k:
        return "o"
    else:
        return find_char(n - prev_length - 3 - k)


N = int(input())
print(find_char(N))
