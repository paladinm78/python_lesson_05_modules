"""
В модуле написать тесты для встроенных функций filter, map, sorted,
а также для функций из библиотеки math: pi, sqrt, pow, hypot.
Чем больше тестов на каждую функцию - тем лучше
"""
import math


def test_filter_even():
    test_list = [1, 2, 3, 4, 5, 6]
    filter_result = filter(lambda x: x % 2 == 0, test_list)
    assert list(filter_result) == [2, 4, 6]


def test_filter_none():
    test_list = [0, 1, False, True, 0.0, 1.1]
    filter_result = filter(None, test_list)
    assert list(filter_result) == [1, True, 1.1]


def test_map_power():
    test_list = [1, 2, 3, 4]
    map_result = map(lambda x: x ** 2, test_list)
    assert list(map_result) == [1, 4, 9, 16]


def test_sorted_asc():
    test_list = [4, 3, 1, 2]
    result = sorted(test_list)
    assert list(result) == [1, 2, 3, 4]


def test_sorted_desc():
    test_list = [4, 3, 1, 2]
    result = sorted(test_list, reverse=True)
    assert list(result) == [4, 3, 2, 1]


def test_pi():
    pi_test = math.pi
    assert pi_test == 3.141592653589793


def test_sqrt_4():
    sqrt_test = math.sqrt(4)
    assert sqrt_test == 2


def test_sqrt_16():
    sqrt_test = math.sqrt(16)
    assert sqrt_test == 4


def test_pow_2_2():
    pow_test = math.pow(2, 2)
    assert pow_test == 4


def test_pow_2_sqrt():
    pow_test = math.pow(2, 1/2)
    assert pow_test == math.sqrt(2)


def test_hypot_pyth():
    hypot_test = math.hypot(3, 4)
    assert hypot_test == 5


def test_hypot_zero():
    hypot_test = math.hypot(0.0, 0)
    assert hypot_test == 0
