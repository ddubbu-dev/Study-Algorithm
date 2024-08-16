N = int(input("정수를 몇 개 저장할까요?:"))
arr = [None] * N

cnt = 0

while True:
    if cnt >= N:
        retry = input(f"계속 할까요? (y/n)")

        if retry in ["N", "n"]:
            exit()

    arr[cnt % N] = int(input(f"{cnt+1}번째 정수를 입력하세요: "))
    cnt += 1

    print(f"arr={arr}\n")
