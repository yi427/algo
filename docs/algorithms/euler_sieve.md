# 欧拉筛（线性筛）

## 算法原理

欧拉筛（Euler Sieve）是一种线性时间复杂度的质数筛选算法，也称为线性筛。相比埃拉托斯特尼筛法（埃氏筛），欧拉筛保证每个合数只被其最小质因子筛选一次，从而达到 O(n) 的时间复杂度。

**核心思想：**
- 维护一个最小质因数数组 spf（Smallest Prime Factor）
- 每个合数只被它的最小质因子标记一次
- 当 i % p == 0 时停止内层循环，避免重复标记

**关键优化：**
- 当 `i % p == 0` 时，p 是 i 的最小质因子，此时 `i * p` 的最小质因子也是 p
- 继续遍历更大的质数会导致重复标记，因此提前 break

## 实现方式

### Python 实现

```python
def euler_sieve(n):
    spfs = list(range(n + 1))
    primes = []

    for i in range(2, n + 1):
        if spfs[i] == i:
            primes.append(i)

        for p in primes:
            if i * p > n:
                break
            spfs[i * p] = p
            if i % p == 0:
                break

    return spfs
```

**返回值：**
- `spfs[i]` 表示 i 的最小质因子
- `primes` 列表包含所有质数

### Swift 实现

```swift
class PrimeHelper {
    private let spf: [Int]
    private let primes: [Int]
    private let n: Int

    init(_ n: Int) {
        self.n = n
        var spf = Array(0...n)
        var primes: [Int] = []
        assert(n >= 2)

        for i in 2...n {
            if spf[i] == i {
                primes.append(i)
            }
            for prime in primes {
                if i * prime > n { break }
                spf[i * prime] = prime
                if i % prime == 0 { break }
            }
        }
        self.spf = spf
        self.primes = primes
    }

    func isPrime(_ x: Int) -> Bool {
        assert(x >= 2 && x <= n)
        return spf[x] == x
    }

    func factorize(_ x: Int) -> [(prime: Int, exp: Int)] {
        assert(x >= 2 && x <= n)
        var x = x
        var result: [(prime: Int, exp: Int)] = []

        while x > 1 {
            let p = spf[x]
            var exp = 0
            while x > 1 && spf[x] == p {
                x /= p
                exp += 1
            }
            result.append((p, exp))
        }

        return result
    }
}
```

## 应用场景

1. **质数生成**：快速生成 n 以内的所有质数
2. **质因数分解**：利用最小质因子数组快速分解任意数
3. **欧拉函数**：计算多个数的欧拉函数值
4. **数论问题**：需要频繁判断质数或分解质因数的场景

## 复杂度分析

- **时间复杂度**：O(n)，每个合数只被标记一次
- **空间复杂度**：O(n)，存储 spf 数组和质数列表

## 相关模板

- [Python 欧拉筛模板](../../templates/python/euler_sieve.py)
- [Swift 质数工具模板](../../templates/swift/prime.swift)

## 与埃氏筛的对比

| 特性 | 埃氏筛 | 欧拉筛 |
|------|--------|--------|
| 时间复杂度 | O(n log log n) | O(n) |
| 实现难度 | 简单 | 中等 |
| 额外信息 | 仅质数列表 | 最小质因子数组 |
| 适用场景 | 简单质数筛选 | 需要质因数分解 |
