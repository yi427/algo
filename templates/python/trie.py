
class Trie:
    def __init__(self) -> None:
        self.children: list[Trie | None] = [None, None]

    def insert(self, num: int):
        root = self

        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            assert root
            if not root.children[bit]:
                root.children[bit] = Trie()
            root = root.children[bit]
