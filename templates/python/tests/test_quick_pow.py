import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

import pytest
from quick_pow import quick_pow


@pytest.mark.parametrize(
    "x, n, expected",
    [
        (2.0, 3, 8.0),
        (3.0, 4, 81.0),
        (1.0, 100, 1.0),
    ],
)
def test_positive_power(x, n, expected):
    assert quick_pow(x, n) == expected


# 2. 批量测试 0 次幂
@pytest.mark.parametrize("x", [5.0, -5.0, 0.0])
def test_zero_power(x):
    assert quick_pow(x, 0) == 1.0


# 3. 测试负数次幂与小数底数 (使用 pytest.approx 解决浮点数精度问题)
@pytest.mark.parametrize(
    "x, n, expected",
    [
        (2.0, -2, 0.25),
        (10.0, -1, 0.1),
        (2.0, -3, 0.125),
        (0.5, 2, 0.25),
        (1.5, 3, 3.375),
    ],
)
def test_float_results(x, n, expected):
    # pytest.approx 相当于 unittest 中的 assertAlmostEqual
    assert quick_pow(x, n) == pytest.approx(expected)


# 4. 测试负数底数 (奇偶次幂符号变化)
def test_negative_base():
    assert quick_pow(-2.0, 2) == 4.0  # 偶数次幂
    assert quick_pow(-2.0, 3) == -8.0  # 奇数次幂


# 5. 测试异常捕获：底数为 0 且指数为负数
def test_zero_base_exceptions():
    assert quick_pow(0.0, 5) == 0.0

    # 使用 pytest.raises 来捕获预期的异常
    with pytest.raises(ZeroDivisionError):
        quick_pow(0.0, -1)
