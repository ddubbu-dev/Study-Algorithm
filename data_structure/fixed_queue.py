from typing import Any
from enum import Enum
from collections import deque


class FixedQueue:
    def __init__(self, capacity: int) -> None:
        self.que = deque([], maxlen=capacity)

    def __contains__(self, value: Any) -> bool:
        return self.count(value) > 0

    def get_size(self) -> int:
        return len(self.que)

    def is_empty(self) -> bool:
        return self.get_size() <= 0

    def is_full(self) -> bool:
        return self.get_size() >= self.capacity

    def enque(self, x: Any) -> None:
        self.que.append(x)

    def deque(self) -> Any:
        return self.que.popleft()

    def peek(self) -> Any:
        return self.que[0]

    def find(self, value: Any) -> Any:
        return self.que.index(value)

    def count(self, value: Any) -> bool:
        return self.que.count(value)

    def clear(self) -> None:
        self.que.clear()

    def print_from_front_to_rear(self):
        if self.is_empty():
            print("Empty!")
        else:
            for idx in range(self.get_size()):
                print(self.que[(idx)], end=" ")
            print()


capaicty = 64
q = FixedQueue(capaicty)

Menu = Enum("Menu", ["인큐", "디큐", "피크", "검색", "순회", "종료"])


def select_menu() -> Menu:
    S = [f"{m.value}{m.name}" for m in Menu]
    while True:
        print(*S, sep=" ", end="")
        n = int(input(": "))
        if 1 <= n <= len(Menu):
            return Menu(n)
        else:
            return "유효하지 않는 명령어 입니다."


while True:
    print(f"현재 데이터 개수: {q.get_size()} / {capaicty}")
    menu = select_menu()

    if menu == Menu.인큐:
        x = int(input("인큐할 데이터를 입력하세요.: "))
        try:
            q.enque(x)
        except FixedQueue.Full:
            print("큐가 가득 찼습니다.")

    elif menu == Menu.디큐:
        try:
            x = q.deque()
            print(f"디큐한 데이터는 {x}입니다.")
        except FixedQueue.Empty:
            print("큐가 비어 있습니다.")
    elif menu == Menu.피크:
        try:
            x = q.peek()
            print(f"피크한 데이터는 {x}입니다.")
        except FixedQueue.Empty:
            print("큐가 비어 있습니다.")

    elif menu == Menu.검색:
        x = int(input("검색할 값을 입력하세요.: "))
        if x in q:
            print(f"{q.count(x)}개 포함되고, 맨 앞의 위치는 {q.find(x)}입니다.")
        else:
            print("검색값을 찾을 수 없습니다.")

    elif menu == Menu.순회:
        q.print_from_front_to_rear()

    else:
        exit()
