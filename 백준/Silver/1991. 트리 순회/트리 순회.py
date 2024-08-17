
"""
[참고 자료](https://thisismi.tistory.com/entry/%EB%B0%B1%EC%A4%80-1991%EB%B2%88-%ED%8A%B8%EB%A6%AC-%EC%88%9C%ED%9A%8C-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%ED%92%80%EC%9D%B4)
[꿀팁]
- 트리라고 무조건 class 정의할 필요는 없다. dictioary로 vertex, edge 관리해도 충분하다.

[주의사항]
- 단순히 child를 쌓으면, left, right 개념이 사라짐. 해서 순서 보장해줘야함.
"""

from collections import deque

# import sys
# readline = lambda: sys.stdin.readline().strip()

readline = input

T = int(readline())

tree = {}


for _ in range(T):
    root, left, right = readline().split()
    child = [left, right]
    tree[root] = child


def preorder(root):
    if root == ".":
        return

    print(root, end="")
    preorder(tree[root][0])
    preorder(tree[root][1])


def inorder(root):
    if root == ".":
        return

    inorder(tree[root][0])
    print(root, end="")
    inorder(tree[root][1])


def postorder(root):
    if root == ".":
        return

    postorder(tree[root][0])
    postorder(tree[root][1])
    print(root, end="")


preorder("A")
print()
inorder("A")
print()
postorder("A")
