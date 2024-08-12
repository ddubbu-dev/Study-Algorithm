"""

[문제 이해]
- A1 ~ An 수열 주어짐
- (+) (-) (x) (//)
- 만들 수 있는 수식의 최댓값, 최솟값 출력

[핵심]
- 어떻게 [3,1,0,2] 와 같은 리스트 값을 탐색할 수 있을까?

"""

OP_ADD = 0
OP_SUB = 1
OP_MUL = 2
OP_DIV = 3


def calculate(operator_idx, a, b):
    operator_characters = ["+", "-", "x", "//"]

    # print(f"{a} {operator_characters[operator_idx]} {b}")

    if operator_idx == OP_ADD:
        return a + b
    elif operator_idx == OP_SUB:
        return a - b
    elif operator_idx == OP_MUL:
        return a * b
    else:
        if a > 0:
            return a // b
        else:
            a = -a
            return -(a // b)


max_result = -1000_000_000 + 1 # 팁) 음수까지 올 수 있음
min_result = 1000_000_000 + 1  # Q. 거의 모든 예제에서 큰수, 작은수를 1e9로 잡는 이유는?


N = int(input())
nums = list(map(int, input().split()))
operators = list(map(int, input().split()))


def dfs(num_idx, result):
    global max_result, min_result
    if num_idx == len(nums):  # 탈출
        max_result = max(result, max_result)
        min_result = min(result, min_result)
        return

    if operators[OP_ADD]:
        operators[OP_ADD] -= 1
        dfs(num_idx + 1, calculate(OP_ADD, result, nums[num_idx]))
        operators[OP_ADD] += 1

    # 주의, 완전탐색인 이유! elif 가 아님
    if operators[OP_SUB]:
        operators[OP_SUB] -= 1
        dfs(num_idx + 1, calculate(OP_SUB, result, nums[num_idx]))
        operators[OP_SUB] += 1

    if operators[OP_MUL]:
        operators[OP_MUL] -= 1
        dfs(num_idx + 1, calculate(OP_MUL, result, nums[num_idx]))
        operators[OP_MUL] += 1

    if operators[OP_DIV]:
        operators[OP_DIV] -= 1
        dfs(num_idx + 1, calculate(OP_DIV, result, nums[num_idx]))
        operators[OP_DIV] += 1


dfs(1, nums[0])

print(max_result)
print(min_result)
