class BinarySearchTree:
    NOT_FOUNDED = -1

    def __init__(self):
        self.tree = []  # 이진 탐색 트리를 리스트로 관리

    def insert(self, value):
        """이진 탐색 트리에 값을 삽입합니다."""
        if len(self.tree) == 0:
            self.tree.append(value)  # 첫 번째 값은 루트로 추가
        else:
            self._insert_recursive(0, value)  # 재귀적으로 삽입

    def _insert_recursive(self, index, value):
        """재귀적으로 값을 삽입하는 헬퍼 메소드입니다."""
        if value < self.tree[index]:  # 왼쪽 서브트리
            left_index = 2 * index + 1
            if left_index >= len(self.tree):
                self.tree.append(value)  # 새로운 노드 추가
            else:
                self._insert_recursive(left_index, value)  # 왼쪽 자식에 재귀 호출
        else:  # 오른쪽 서브트리
            right_index = 2 * index + 2
            if right_index >= len(self.tree):
                self.tree.append(value)  # 새로운 노드 추가
            else:
                self._insert_recursive(right_index, value)  # 오른쪽 자식에 재귀 호출

    def search(self, target):
        return self.search_idx(target) != self.NOT_FOUNDED

    def search_idx(self, target):
        """이진 탐색 트리에서 값을 검색합니다."""
        return self._search_idx_recursive(0, target)

    def _search_idx_recursive(self, index, target):
        """재귀적으로 값을 검색하는 헬퍼 메소드입니다."""
        if index >= len(self.tree):
            return self.NOT_FOUNDED

        if self.tree[index] == target:
            return index

        if target < self.tree[index]:
            return self._search_idx_recursive(2 * index + 1, target)  # 왼쪽 자식 검색
        else:
            return self._search_idx_recursive(2 * index + 2, target)  # 오른쪽 자식 검색
