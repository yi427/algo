# 快速幂算法

## 算法原理

快速幂算法用于高效计算 x^n，将时间复杂度从 O(n) 优化到 O(log n)。

核心思想是利用指数的二进制表示：
- 当 n 为偶数：x^n = (x^2)^(n/2)
- 当 n 为奇数：x^n = x * x^(n-1)

## 实现方式

### 1. 递归实现

```python
def quick_pow(x: float, n: int) -> float:
    if n < 0:
        return 1.0 / quick_pow(x, -n)
    if n == 0:
        return 1.0
    if n & 1:
        return x * quick_pow(x, n - 1)
    return quick_pow(x * x, n // 2)
```

### 2. 迭代实现（带取模）

用于处理大数运算，避免溢出：

```python
def quick_pow_with_mod(x: int, n: int, p: int = 1_000_000_007) -> int:
    res = 1 % p
    x = x % p
    while n > 0:
        if n & 1:
            res = (res * x) % p
        x = (x * x) % p
        n >>= 1
    return res
```

### 3. Swift 实现

```swift
func quick_pow(_ x: Double, _ n: Int) -> Double {
    var base = x, power = n.magnitude
    var res: Double = 1.0
    while power > 0 {
        if power & 1 == 1 {
            res *= base
        }
        base *= base
        power >>= 1
    }
    return n < 0 ? 1.0 / res : res
}
```

