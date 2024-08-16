from typing import Any
from enum import Enum


class FixedQueue:
    class Empty(Exception):
        pass

    class Full(Exception):
        pass

    def __init__(self, capacity: int) -> None:
        self.cnt = 0
        self.front = 0
        self.rear = 0
        self.capacity = capacity
        self.que = [None] * capacity

    def __len__(self) -> int:
        return self.cnt  # Q. abs(self.front - self.rear) 아닌가?

    def is_empty(self) -> bool:
        return self.cnt <= 0

    def is_full(self) -> bool:
        return self.cnt >= self.capacity

    def __contains__(self, value: Any) -> bool:
        return self.count(value) > 0

    def enque(self, x: Any) -> None:
        if self.is_full():
            raise FixedQueue.Full

        self.que[self.rear] = x
        self.rear = (self.rear + 1) % self.capacity  # 원형 구조
        self.cnt += 1

    def deque(self) -> Any:
        if self.is_empty():
            raise FixedQueue.Empty

        x = self.que[self.front]
        self.front = (self.front + 1) % self.capacity
        self.cnt -= 1

        return x

    def peek(self) -> Any:
        if self.is_empty():
            raise FixedQueue.Empty
        return self.que[self.front]

    def find(self, value: Any) -> Any:
        for i in range(self.cnt):
            idx = (i + self.front) % self.capacity
            if self.que[idx] == value:
                return idx
        return -1

    def count(self, value: Any) -> bool:
        result = 0

        for i in range(self.cnt):
            idx = (i + self.front) % self.capacity
            if self.que[idx] == value:
                result += 1

        return result

    def clear(self) -> None:
        # self.__init__(self.capacity)
        self.cnt = self.front = self.rear = 0

    def print_from_front_to_rear(self):
        if self.is_empty():
            print("Empty!")
        else:
            for idx in range(self.cnt):
                print(self.que[(idx + self.front) % self.capacity], end=" ")
            print()


q = FixedQueue(64)


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
    print(f"현재 데이터 개수: {len(q)} / {q.capacity}")
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
