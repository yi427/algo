class QuickPow:
    @staticmethod
    def pow(x: float, n: int) -> float:
        if n < 0:
            return 1.0 / QuickPow.pow(x, -n)

        if n == 0:
            return 1.0

        if n & 1:
            return x * QuickPow.pow(x, n - 1)
        return QuickPow.pow(x * x, n // 2)

    @staticmethod
    def pow_mod(x: int, n: int, p: int = 1_000_000_007) -> int:
        assert n >= 0
        res = 1 % p
        x = x % p
        while n > 0:
            if n & 1:
                res = (res * x) % p
            x = (x * x) % p
            n >>= 1
        return res


if __name__ == "__main__":
    a, b, p = list(map(int, input().split()))
    res = QuickPow.pow_mod(a, b, p)
    print(f"{a}^{b} mod {p}={res}")
