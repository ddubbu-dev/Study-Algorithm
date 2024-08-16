from typing import Any
from collections import deque


class FixedStack:
    def __init__(self, capacity: int) -> None:
        self.stk = deque([], capacity)
        self.capacity = capacity

    def __len__(self) -> int:
        """dunder함수; len() 함수에 전달 가능"""
        return len(self.stk)

    def __contains__(self, value: Any) -> bool:
        """dunder함수; 멤버 판단 연산자 in 적용 가능"""
        return self.count(value) > 0

    def is_empty(self) -> bool:
        return not self.stk

    def is_full(self) -> bool:
        return self.__len__ == self.capacity

    def push(self, value: Any) -> None:
        self.stk.append(value)

    def pop(self) -> Any:
        return self.stk.pop()

    def peek(self) -> Any:
        return self.stk[-1]

    def clear(self) -> None:
        return self.stk.clear()

    def find(self, value: Any) -> Any:
        try:
            return self.stk.index(value)
        except ValueError:
            return -1

    def count(self, value: Any) -> int:
        return self.stk.count(value)

    def print_from_bottom_to_top(self) -> None:
        print(list(self.stk))


from enum import Enum

Menu = Enum("Menu", ["푸시", "팝", "피크", "검색", "순회", "종료"])

print(Menu)


def select_menu() -> Menu:
    S = [f"{m.value}{m.name}" for m in Menu]
    while True:
        print(*S, sep=" ", end="")
        n = int(input(": "))
        if 1 <= n <= len(Menu):
            return Menu(n)
        else:
            return "유효하지 않는 명령어 입니다."


s = FixedStack(64)

while True:
    print(f"현재 데이터 개수: {len(s)} / {s.capacity}")
    menu = select_menu()

    if menu == Menu.푸시:
        x = int(input("데이터를 입력하세요.: "))
        try:
            s.push(x)
        except FixedStack.Full:
            print("스택이 가득차 있습니다.")

    elif menu == Menu.팝:
        try:
            s.pop()
            print(f"팝한 데이터는 {x}입니다.")
        except FixedStack.Empty:
            print("스택이 비어 있습니다.")

    elif menu == Menu.피크:
        try:
            x = s.peek()
            print(f"피크한 데이터는 {x}입니다.")
        except FixedStack.Empty:
            print("스택이 비어 있습니다.")

    elif menu == Menu.검색:
        x = int(input("검색할 값을 입력하세요.: "))
        if x in s:
            print(f"{s.count(x)}개 포함되고, 맨 앞의 위치는 {s.find(x)}입니다.")
        else:
            print("검색값을 찾을 수 없습니다.")

    elif menu == Menu.순회:
        s.print_from_bottom_to_top()

    elif menu == Menu.종료:
        break