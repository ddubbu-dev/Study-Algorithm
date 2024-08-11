"""
[핵심]
- 재귀라면, f(n)을 찾을 수 있어야한다.
"""

MOVE_TARGET_BAR_IDX = 3
N = int(input())

"""
[참고자료](https://hongong.hanbit.co.kr/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9E%AC%EA%B7%80-%ED%95%A8%EC%88%98-%ED%95%98%EB%85%B8%EC%9D%B4-%ED%83%91/)
- 뭉텅이 그림 예쁘다
"""


# height = 옮겨야 할 하노이 그룹 높이
def move(height, from_bar_idx, to_bar_idx):
    if height == 1:
        print(from_bar_idx, to_bar_idx)
        return

    sub하노이_to_bar_idx = 6 - from_bar_idx - to_bar_idx
    # 같은 기둥 위에 있는 sub-하노이를 옮기기
    move(height - 1, from_bar_idx, sub하노이_to_bar_idx)
    print(from_bar_idx, to_bar_idx)
    move(height - 1, sub하노이_to_bar_idx, to_bar_idx)  # 주의) 변수화 필요


"""
[python 시간초과 해결 방법]
- 등비수열 점화식을 통해 이동 횟수 구하기
- [참고자료](https://zeun-dev.tistory.com/9)

f(n); 이동횟수
f(n) = 2xf(n-1)+1; sub-하노이x2번 옮김 + main하노이 base 1번 옮김

f(n)+1 = 2xf(n-1)+2
b(n) = 2xb(n-1); r=2 등비수열 (a_n = a_1 x r^(n-1))

f(1) = 1, b(1) = 2; 초기값
b(n) = b(1)x(2)^(n-1) = 2^n = f(n)+1

따라서 f(n) = 2^n -1
"""
print(2**N - 1)

if N <= 20:
    move(N, 1, MOVE_TARGET_BAR_IDX)
