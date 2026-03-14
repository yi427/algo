# 字典树（Trie / 前缀树）

## 基本概念

字典树（Trie）是一种树形数据结构，用于高效地存储和检索字符串或数字的集合。本文档介绍的是二进制字典树，专门用于处理整数的位运算问题。

**主要功能：**
- 插入（Insert）：将一个数字的二进制表示插入到树中
- 查找（Search）：在树中查找与给定数字异或值最大的数字
- 前缀匹配：利用二进制位的前缀特性进行高效查询

**应用场景：**
- 最大异或值问题
- 异或相关的数组问题
- 位运算优化
- 前缀匹配查询

## 核心操作

### 1. 初始化

二进制字典树每个节点有两个子节点，分别代表 0 和 1。

```python
def __init__(self) -> None:
    self.children: list[Trie | None] = [None, None]
```

### 2. 插入（Insert）

将数字的二进制表示从高位到低位依次插入树中。

```python
def insert(self, num: int):
    root = self
    for i in range(31, -1, -1):
        bit = (num >> i) & 1
        if not root.children[bit]:
            root.children[bit] = Trie()
        root = root.children[bit]
```

**说明：**
- 从最高位（第 31 位）开始遍历
- 提取每一位的值（0 或 1）
- 如果对应子节点不存在则创建
- 移动到子节点继续处理下一位

### 3. 查找最大异或值

在树中查找与给定数字异或值最大的路径。

```python
def find_max_xor(self, num: int) -> int:
    node = self
    xor = 0
    for i in range(31, -1, -1):
        bit = (num >> i) & 1
        not_bit = 0 if bit == 1 else 1
        # 优先选择相反的位以最大化异或值
        if node.children[not_bit]:
            node = node.children[not_bit]
            xor |= not_bit << i
        else:
            node = node.children[bit]
            xor |= bit << i
    return xor ^ num
```

## 完整实现

### Python 实现

```python
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
```

### Swift 实现

```swift
class Trie {

    public var children: [Trie?]

    init() {
        children = Array(repeating: nil, count: 2)
    }

     func insert(_ num: Int) {
         var root = self
         for i in (0..<32).reversed() {
             let bit = (num >> i) & 1
             if root.children[bit] == nil {
                 root.children[bit] = Trie()
             }
             root = root.children[bit]!
         }
    }
}
```

## 使用示例

```python
# 创建字典树并插入数字
trie = Trie()
nums = [3, 10, 5, 25, 2, 8]
for num in nums:
    trie.insert(num)

# 查找与每个数字异或值最大的结果
max_xor = 0
for num in nums:
    node, xor = trie, 0
    for i in range(31, -1, -1):
        bit = (num >> i) & 1
        not_bit = 0 if bit == 1 else 1
        if node.children[not_bit]:
            node = node.children[not_bit]
            xor |= not_bit << i
        else:
            node = node.children[bit]
            xor |= bit << i
    max_xor = max(max_xor, xor ^ num)

print(max_xor)  # 输出: 28 (5 XOR 25)
```

## 复杂度分析

- **插入操作**：O(32) = O(1)，固定遍历 32 位
- **查找操作**：O(32) = O(1)，固定遍历 32 位
- **空间复杂度**：O(n × 32)，其中 n 是插入的数字个数

## 相关模板

- [Python 字典树模板](../../templates/python/trie.py)
- [Swift 字典树模板](../../templates/swift/trie.swift)

## 相关题目

- [LeetCode 421. 数组中两个数的最大异或值](../../problems/leetcode/421.md)
