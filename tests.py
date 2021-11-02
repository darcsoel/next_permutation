# import pytest

from main import Solution


def test_1():
    initial = [1, 2, 3]
    Solution().nextPermutation(initial)
    assert initial == [1, 3, 2]


def test_2():
    initial = [3, 2, 1]
    Solution().nextPermutation(initial)
    assert initial == [1, 2, 3]


def test_3():
    initial = [1, 1, 5]
    Solution().nextPermutation(initial)
    assert initial == [1, 5, 1]


def test_4():
    initial = [1]
    Solution().nextPermutation(initial)
    assert initial == [1]


def test_5():
    initial = [1, 3, 2]
    Solution().nextPermutation(initial)
    assert initial == [2, 1, 3]


def test_6():
    initial = [2, 3, 1]
    Solution().nextPermutation(initial)
    assert initial == [3, 1, 2]


def test_7():
    initial = [2, 3, 1, 3, 3]
    Solution().nextPermutation(initial)
    assert initial == [2, 3, 3, 1, 3]
