def is_prime(target):

    # 예외처리
    if target == 1:
        return False

    elif target != 2 and target % 2 == 0:
        return False

    for i in range(2, target):  # 자기 미포함
        if target % i == 0:
            return False

    return True
