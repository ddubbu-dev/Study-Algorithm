target_n = int(input())
cnt = 1

start_n = target_n


def get_digits(num):
    if num < 10:
        return [0, num]
    elif 10 <= num and num <= 99:
        return [num // 10, num % 10]


while True:
    nums_arr = get_digits(start_n)

    added_digits = get_digits(sum(nums_arr))

    start_n = int(f"{nums_arr[-1]}{added_digits[-1]}")
    if start_n == target_n:
        break
    cnt += 1


print(cnt)
