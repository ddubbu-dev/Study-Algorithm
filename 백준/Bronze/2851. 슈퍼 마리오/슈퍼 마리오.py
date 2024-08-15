
N = 10
COMPARE_VALUE = 100

prev_acc = 0

step = 1
while step <= N:
    new_score = int(input())
    acc = prev_acc + new_score

    if abs(prev_acc - COMPARE_VALUE) >= abs(acc - COMPARE_VALUE):
        prev_acc = acc
        step += 1
        continue

    break

print(prev_acc)
