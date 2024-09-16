"""
[문제 이해]
- best_pizza: 1원당 열량이 높은 피자
- 토핑 N개 중에 선택, 같은 종류 안됨 / 전부 미선택도 가능
- best_pizza 열량 구하기

[시도1]
- 우선 토핑 에너지순으로 내림차순, 그리디 후 열량 계산해서 best pizza 갱신

[반례]
- 토핑을 아예 고르지 않는 경우
"""

import sys
readline = lambda: sys.stdin.readline().strip()

# 전처리
n = int(readline())
dough_price, topping_price = map(int, readline().split())
dough_energy = int(readline())
topping_energies = []
for i in range(n):
    topping_energies.append(int(readline()))
topping_energies.sort(reverse=True)


def get_energy_per_price(picked_cnt):
    picked_toppings = topping_energies[:picked_cnt]
    sum_energy = dough_energy + sum(picked_toppings)
    sum_price = dough_price + topping_price * picked_cnt

    return sum_energy / sum_price


max_energy_per_price = 0

for picked_cnt in range(0, n + 1):
    result = get_energy_per_price(picked_cnt)
    max_energy_per_price = max(max_energy_per_price, result)

print(f"{int(max_energy_per_price)}")
