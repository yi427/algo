class Dsu:
    def __init__(self, n: int) -> None:
        self._parent_or_size = [-1] * n
        self._n = n
        self._counter = n

    def is_root(self, n: int) -> bool:
        assert 0 <= n < self._n
        return self._parent_or_size[n] < 0

    def connected(self) -> int:
        return self._counter

    def size(self, node: int) -> int:
        root = self.find_set(node)
        return -self._parent_or_size[root]

    def find_set(self, node: int) -> int:
        if self.is_root(node):
            return node
        parent = self.find_set(self._parent_or_size[node])
        self._parent_or_size[node] = parent
        return parent

    def union_set(self, x: int, y: int) -> int:
        x = self.find_set(x)
        y = self.find_set(y)
        if x == y:
            return x

        if -self._parent_or_size[x] < -self._parent_or_size[y]:
            x, y = y, x

        self._parent_or_size[x] += self._parent_or_size[y]
        self._parent_or_size[y] = x
        self._counter -= 1
        return x
