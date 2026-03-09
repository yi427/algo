def quick_pow(x: float, n: int) -> float:
    if n < 0:
        return 1.0 / quick_pow(x, -n)

    if n == 0:
        return 1.0

    if n & 1:
        return x * quick_pow(x, n - 1)
    return quick_pow(x * x, n // 2)
