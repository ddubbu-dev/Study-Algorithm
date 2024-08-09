
"""
Q. 이게 왜 재귀 문제인가?
Answer.
- 카드를 뽑는 액션이 계속 반복됨. 
- 또한 몇번을 반복할지 모르는 상황에서 for문을 사용할 수 없음
"""


n = int(input())
k = int(input())

# 카드 만들기
raw_cards = []  # {picked: Bool; num: Int}
for i in range(n):
    num = int(input())
    card = {"num": num}
    card["picked"] = False
    raw_cards.append(card)

generated_nums = []


# 주의)
# - search_idx 뒤에서부터 시작해도 앞에 뽑을 수 있음
# - 그리고 조합이 아니라 순열이라 순서 중요함
def get_collection(picked_nums, search_idx):
    if search_idx >= len(raw_cards):
        return

    if len(picked_nums) == k:  # 재귀 - 탈출
        # print(f"raw_cards: {raw_cards}")
        # print(f"picked_nums: {picked_nums}")
        picked_nums_str = map(str, picked_nums)

        # 주의) join 은 str 요소만 가능
        generated_num = int("".join(picked_nums_str))
        generated_nums.append(generated_num)
        return

    if not raw_cards[search_idx]["picked"]:
        raw_cards[search_idx]["picked"] = True
        picked_num = raw_cards[search_idx]["num"]
        picked_nums.append(picked_num)

        get_collection(picked_nums, 0)  # 주의) 순열이라, 처음부터 다시 찾기

        # 재귀 - 복구
        picked_nums.pop()
        raw_cards[search_idx]["picked"] = False

    # 재귀 - 호출
    get_collection(picked_nums, search_idx + 1)  # 그 다음부터 찾기


get_collection([], 0)
no_duplicated = list(set(generated_nums))

print(len(no_duplicated))
