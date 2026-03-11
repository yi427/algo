# 并查集（Disjoint Set Union）

## 基本概念

并查集（DSU）是一种树型的数据结构，用于处理一些不相交集合的合并及查询问题。

**主要功能：**
- 查找（Find）：确定某个元素属于哪个集合
- 合并（Union）：将两个集合合并为一个集合
- 判断连通性：判断两个元素是否在同一个集合中

**应用场景：**
- 判断图的连通性
- 最小生成树算法（Kruskal）
- 动态连通性问题
- 朋友圈问题

## 核心操作

### 1. 初始化

初始时，每个元素都是一个独立的集合，父节点指向自己。

```python
def __init__(self, n: int):
    self._parent_or_size = [-1] * n  # 负数表示根节点，值为集合大小的相反数
    self._n = n
    self._counter = n  # 连通分量个数
```

### 2. 查找（Find）

查找元素所属集合的根节点，同时进行路径压缩优化。

```python
def find_set(self, node: int) -> int:
    if self.is_root(node):
        return node
    parent = self.find_set(self._parent_or_size[node])
    self._parent_or_size[node] = parent  # 路径压缩
    return parent
```

### 3. 合并（Union）

将两个集合合并，使用按秩合并优化。

```python
def union_set(self, x: int, y: int) -> int:
    x = self.find_set(x)
    y = self.find_set(y)
    if x == y:
        return x

    # 按大小合并，小树挂到大树上
    if -self._parent_or_size[x] < -self._parent_or_size[y]:
        x, y = y, x

    self._parent_or_size[x] += self._parent_or_size[y]
    self._parent_or_size[y] = x
    self._counter -= 1
    return x
```

## 优化技巧

### 1. 路径压缩（Path Compression）

在查找过程中，将路径上的所有节点直接连接到根节点，降低树的高度。

**效果**：使得后续查找操作更快，接近 O(1)。

### 2. 按秩合并（Union by Rank/Size）

合并时，将较小的树挂到较大的树上，避免树退化成链表。

**效果**：保持树的平衡，降低树的高度。

## 辅助方法

```python
def is_root(self, n: int) -> bool:
    """判断节点是否为根节点"""
    return self._parent_or_size[n] < 0

def connected(self) -> int:
    """返回连通分量个数"""
    return self._counter

def size(self, node: int) -> int:
    """返回节点所在集合的大小"""
    root = self.find_set(node)
    return -self._parent_or_size[root]
```

## 复杂度分析

- **时间复杂度**：
  - 初始化：O(n)
  - 查找：O(α(n))，α 为阿克曼函数的反函数，增长极慢，可视为常数
  - 合并：O(α(n))

- **空间复杂度**：O(n)

## 完整实现

```python
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
```

## 使用示例

```python
# 创建包含 5 个元素的并查集
dsu = Dsu(5)

# 合并元素
dsu.union_set(0, 1)
dsu.union_set(2, 3)

# 查询
print(dsu.find_set(0) == dsu.find_set(1))  # True
print(dsu.find_set(0) == dsu.find_set(2))  # False

# 查询连通分量个数
print(dsu.connected())  # 3

# 查询集合大小
print(dsu.size(0))  # 2
```
